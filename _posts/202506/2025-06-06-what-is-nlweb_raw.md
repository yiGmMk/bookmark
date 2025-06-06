---
layout: post
---
Title: What is NLWeb?

URL Source: https://glama.ai/blog/2025-06-01-what-is-nlweb

Markdown Content:
Microsoft recently open-sourced [NLWeb](https://github.com/microsoft/NLWeb), a protocol for adding conversational interfaces to websites.[1](https://glama.ai/blog/2025-06-01-what-is-nlweb#user-content-fn-1) It leverages [Schema.org](https://schema.org/) structured data that many sites already have and includes built-in support for MCP (Model Context Protocol), enabling both human conversations and agent-to-agent communication.

**The key idea:** NLWeb creates a standard protocol that turns any website into a conversational interface that both humans and AI agents can query naturally.

**Want to try NLWeb?**

As part of writing this post, I've implemented NLWeb search for MCP servers. Refer to the "Glama NLWeb Server" section for examples.

What Problem Does NLWeb Solve?
------------------------------

Currently, websites have structured data (Schema.org) but no standard way for AI agents or conversational interfaces to access it. Every implementation is bespoke. Traditional search interfaces struggle with context-aware, multi-turn queries.

NLWeb creates a standard protocol for conversational access to web content. Like RSS did for syndication, NLWeb does for AI interactions - one implementation serves both human chat interfaces and programmatic agent access.

The key insight: Instead of building custom NLP for every site, NLWeb leverages LLMs' existing understanding of Schema.org to create instant conversational interfaces.

The real power comes from multi-turn conversations that preserve context:

1.   "Find recipes for dinner parties"
2.   "Only vegetarian options"
3.   "That can be prepared in under an hour"

Each query builds on the previous context - something traditional search interfaces struggle with.

How NLWeb Works
---------------

### Two-Component System

1.   **Protocol Layer**: REST API (`/ask` endpoint) and MCP server (`/mcp` endpoint) that accept natural language queries and return Schema.org JSON responses
2.   **Implementation Layer**: Reference implementation that orchestrates multiple LLM calls for query processing

### Query Processing Pipeline

User Query → Parallel Pre-processing → Vector Retrieval → LLM Ranking → Response ├─ Relevancy Check ├─ Decontextualization ├─ Memory Detection └─ Fast Track Path

In this flow, a single query may trigger 50+ targeted LLM calls for:

*   Query decontextualization based on conversation history
*   Relevancy scoring against site content
*   Result ranking with custom prompts per content type
*   Optional post-processing (summarization/generation)

The "fast track" optimization launches a parallel path to retrieval (step 3) while pre-processing occurs, but results are blocked until relevancy checks complete[2](https://glama.ai/blog/2025-06-01-what-is-nlweb#user-content-fn-2).

### Video Explanation

After I wrote this article, I was sent this video which includes a great introduction to NLWeb by R.V. Guha (creator of Schema.org, RSS, and RDF):

### Why 50+ LLM Calls?

Instead of using one large prompt to handle everything, NLWeb breaks each query into dozens of small, specific questions:

*   "Is this query about recipes?"
*   "Does it reference something mentioned earlier?"
*   "Is the user asking to remember dietary preferences?"
*   "How relevant is this specific result?"

This approach has two major benefits:

1.   **No hallucination** - Results only come from your actual database
2.   **Better accuracy** - Each LLM call has one clear job it can do well

Think of it like having a team of specialists instead of one generalist.

Even if you don't use NLWeb, this pattern—using many focused LLM calls instead of one complex prompt—is worth borrowing.

Quick Start
-----------

The best way to wrap your head around NLWeb is to try it out.

Microsoft provides a [quick start guide](https://github.com/microsoft/NLWeb/blob/main/docs/nlweb-hello-world.md) for setting up an example NLWeb server with [Behind The Tech](https://www.microsoft.com/en-us/behind-the-tech) RSS feed.

# Setup git clone https://github.com/microsoft/NLWeb cd NLWeb python -m venv myenv source myenv/bin/activate cd code pip install -r requirements.txt # Configure (copy .env.template → .env, update API keys) # Load data python -m tools.db_load https://feeds.libsyn.com/121695/rss Behind-the-Tech # Run python app-file.py

Go to [localhost:8000](http://localhost:8000/) and you should have a working NLWeb server.

I have also noticed that the repository contains a [CLI](https://github.com/microsoft/NLWeb/blob/main/docs/nlweb-cli.md) to simplify configuration, testing, and execution of the application. However, I struggled to get it working.

Once you have the server running, you can ask it questions like:

curl -X POST http://localhost:8000/ask \ -H "Content-Type: application/json" \ -d '{ "query": "tell me more about the first one", "prev": "find podcasts about AI,what topics do they cover" }'

which will return a JSON response like:

{ "query_id": "abc123", "results": [{ "url": "https://...", "name": "AI Safety with Stuart Russell", "score": 85, "description": "Discussion on alignment challenges...", "schema_object": { "@type": "PodcastEpisode", ... } }] }

### Glama NLWeb Server

As part of writing this post, I've built a simple NLWeb server using Node.js. You can use it to query our [MCP server](https://glama.ai/mcp/servers) directory:

curl -X POST https://glama.ai/nlweb/ask \ -H "Content-Type: application/json" \ -d '{"query": "MCP servers for working with GitHub"}'

As far as I can tell, this is the first ever public NLWeb endpoint!

Due to the volume of LLM calls, it takes a few seconds to respond.

or, if you want to continue the conversation:

curl -X POST https://glama.ai/nlweb/ask \ -H "Content-Type: application/json" \ -d '{ "query": "servers that can create PRs", "prev": "MCP servers for working with GitHub" }'

or, if you want to summarize the results:

curl -X POST https://glama.ai/nlweb/ask \ -H "Content-Type: application/json" \ -d '{ "query": "MCP servers for working with GitHub", "mode": "summarize" }'

Useful when you want an overview rather than just a list of results.

or, if you want to generate a response:

curl -X POST https://glama.ai/nlweb/ask \ -H "Content-Type: application/json" \ -d '{ "query": "MCP servers for working with GitHub", "mode": "generate" }'

This mode attempts to answer the question using the retrieved results (like traditional RAG)

Things that made it easy to implement:

*   We have existing embeddings for every MCP server and a vector store
*   We already have a way to make LLM calls

A few questions came to mind as I was implementing this:

*   It seems that NLWeb doesn't dictate where the `/ask` endpoint needs to be hosted—does it have to be `https://glama.ai/ask` or can it be `https://glama.ai/nlweb/ask`?
*   It wasn't super clear to me which Schema.org data is best suited to describe MCP servers.

Not surprisingly, the slowest part of the pipeline is the LLM calls.

REST API
--------

Currently, NLWeb supports two APIs at the endpoints `/ask` and `/mcp`. The arguments are the same for both, as is most of the functionality. The `/mcp` endpoint returns the answers in format that MCP clients can use. The `/mcp` endpoint also supports the core MCP methods (`list_tools`, `list_prompts`, `call_tool` and `get_prompt`).

The `/ask` endpoint supports the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `query` | `string` | Natural language question |
| `site` | `string` | Scope to specific data subset |
| `prev` | `string` | Comma-separated previous queries |
| `decontextualized_query` | `string` | Skip decontextualization if provided |
| `streaming` | `bool` | Enable SSE streaming |
| `query_id` | `string` | Track conversation |
| `mode` | `string` | `list`, `summarize`, or `generate` |

Integrating with MCP
--------------------

Since NLWeb includes an MCP server by default, you can configure Claude for Desktop to talk to NLWeb.

If you already have the NLWeb server running, this should be as simple as adding the following to your `~/Library/Application Support/Claude/claude_desktop_config.json` configuration:

{ "mcpServers": { "ask_nlw": { "command": "/Users/yourname/NLWeb/myenv/bin/python", "args": [ "/Users/yourname/NLWeb/code/chatbot_interface.py", "--server", "http://localhost:8000", "--endpoint", "/mcp" ], "cwd": "/Users/yourname/NLWeb/code" } } }

Implementation Reality
----------------------

The documentation suggests you can get a basic prototype running quickly if you have existing Schema.org markup or RSS feeds.

**What's actually straightforward:**

*   Loading RSS feeds or Schema.org data
*   Basic search functionality with provided prompts
*   Local development with Qdrant

**What requires more effort:**

*   Production deployment at scale
*   Optimizing 50+ LLM calls per query (mentioned in docs)
*   Custom prompt engineering for your domain
*   Maintaining data freshness between vector store and live data

I already had a lot of these components in place, so I was able to get a basic prototype running in an hour. However, to make this production-ready, I'd need to think a lot more time about the cost of the LLM calls.

Should You Care?
----------------

**Yes if:**

*   You have structured data (Schema.org, RSS) already
*   You want to enable conversational search beyond keywords
*   You need programmatic AI agent access via MCP
*   You can experiment with early-stage tech

**No if:**

*   You need battle-tested production code
*   You can't handle significant LLM API costs
*   Your content isn't well-structured
*   You expect plug-and-play simplicity

Bottom Line
-----------

NLWeb is more interesting as a strategic direction than as current technology. NLWeb was conceived and developed by R.V. Guha (creator of Schema.org, RSS, and RDF), now a CVP and Technical Fellow at Microsoft[3](https://glama.ai/blog/2025-06-01-what-is-nlweb#user-content-fn-3). That's serious pedigree.

The O'Reilly prototype proves it's viable for content-heavy sites. The quick start shows it's approachable for developers. But "prototype in days" doesn't mean "production in weeks."

Think of it as an investment in making your content natively conversational. The technical foundation is solid—REST API, standard formats, proven vector stores. The vision is compelling. The code needs work.

Want to experiment? Clone the repo and try the quick start above.

Footnotes
---------

1.   [https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/](https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/)[↩](https://glama.ai/blog/2025-06-01-what-is-nlweb#user-content-fnref-1)

2.   [https://github.com/microsoft/NLWeb](https://github.com/microsoft/NLWeb)[↩](https://glama.ai/blog/2025-06-01-what-is-nlweb#user-content-fnref-2)

3.   [https://techcommunity.microsoft.com/blog/azure-ai-services-blog/nlweb-pioneer-qa-oreilly/4415299](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/nlweb-pioneer-qa-oreilly/4415299)[↩](https://glama.ai/blog/2025-06-01-what-is-nlweb#user-content-fnref-3)

