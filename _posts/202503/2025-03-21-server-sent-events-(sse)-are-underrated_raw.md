---
layout: post
---
Title: Server-Sent Events (SSE) Are Underrated

URL Source: https://igorstechnoclub.com/server-sent-events-sse-are-underrated/

Markdown Content:
_25 Dec, 2024_

Most developers know about WebSockets, but Server-Sent Events (SSE) offer a simpler, often overlooked alternative that deserves more attention. Let's explore why this technology is underrated and how it can benefit your applications.

What are Server-Sent Events?
----------------------------

SSE establishes a one-way communication channel from server to client over HTTP. Unlike WebSockets' bidirectional connection, SSE maintains an open HTTP connection for server-to-client updates. Think of it as a radio broadcast: the server (station) transmits, and clients (receivers) listen.

Why are they Underrated?
------------------------

Two main factors contribute to SSE's underappreciation:

1.  WebSocket's Popularity: WebSockets' full-duplex communication capabilities often overshadow SSE's simpler approach
2.  Perceived Limitations: The unidirectional nature might seem restrictive, though it's often sufficient for many use cases

Key Strengths of SSE
--------------------

### Implementation Simplicity

SSE leverages standard HTTP protocols, eliminating the complexity of WebSocket connection management.

### Infrastructure Compatibility

SSE works seamlessly with existing HTTP infrastructure:

*   Load balancers
*   Proxies
*   Firewalls
*   Standard HTTP servers

### Resource Efficiency

Lower resource consumption compared to WebSockets due to:

*   Unidirectional nature
*   Standard HTTP connection usage
*   No persistent socket maintenance

### Automatic Reconnection

Built-in browser support for:

*   Connection interruption handling
*   Automatic reconnection attempts
*   Resilient real-time experience

### Clear Semantics

One-way communication pattern enforces:

*   Clear separation of concerns
*   Straightforward data flow
*   Simplified application logic

Practical Applications
----------------------

SSE excels in these scenarios:

1.  Real-time News Feeds and Social Updates
2.  Stock Tickers and Financial Data
3.  Progress Bars and Task Monitoring
4.  Server Logs Streaming
5.  Collaborative Editing (for updates)
6.  Gaming Leaderboards
7.  Location Tracking Systems

Implementation Examples
-----------------------

### Server-Side (Flask)

from flask import Flask, Response, stream\_with\_context
import time
import random

app \= Flask(\_\_name\_\_)

def generate\_random\_data():
    while True:
        data \= f"data: Random value: {random.randint(1, 100)}\\n\\n"
        yield data
        time.sleep(1)

@app.route('/stream')
def stream():
    return Response(
        stream\_with\_context(generate\_random\_data()),
        mimetype\='text/event-stream'
    )

if \_\_name\_\_ \== '\_\_main\_\_':
    app.run(debug\=True)

### Client-Side (JavaScript)

const eventSource \= new EventSource("/stream");

eventSource.onmessage \= function(event) {
    const dataDiv \= document.getElementById("data");
    dataDiv.innerHTML += \`<p\>${event.data}</p\>\`;
};

eventSource.onerror \= function(error) {
    console.error("SSE error:", error);
};

Code Explanation
----------------

### Server-Side Components:

*   `/stream` route handles SSE connections
*   `generate_random_data()` continuously yields formatted events
*   `text/event-stream` mimetype signals SSE protocol
*   `stream_with_context` maintains Flask application context

### Client-Side Components:

*   `EventSource` object manages SSE connection
*   `onmessage` handler processes incoming events
*   `onerror` handles connection issues
*   Automatic reconnection handled by browser

* * *

**Like the article so far? Support the author (me)**

[Patreon](https://patreon.com/IgorTechnoclub?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink)

* * *

Limitations and Considerations
------------------------------

When implementing SSE, be aware of these constraints:

### 1\. Unidirectional Communication

*   Server-to-client only
*   Requires separate HTTP requests for client-to-server communication

### 2\. Browser Support

*   [Well-supported](https://caniuse.com/?search=EventSource) in modern browsers
*   May need polyfills for older browsers

### 3\. Data Format

*   Primary support for text-based data
*   Binary data requires encoding (e.g., Base64)

### 4\. Best works with HTTP/2

As stated in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#sect1):

> Warning: When not used over HTTP/2, SSE suffers from a limitation to the maximum number of open connections, which can be especially painful when opening multiple tabs, as the limit is per browser and is set to a very low number (6). The issue has been marked as "Won't fix" in Chrome and Firefox. This limit is per browser + domain, which means that you can open 6 SSE connections across all of the tabs to www.example1.com and another 6 SSE connections to www.example2.com (per Stack Overflow). When using HTTP/2, the maximum number of simultaneous HTTP streams is negotiated between the server and the client (defaults to 100)

Best Practices
--------------

1.  Error Handling

eventSource.onerror \= function(error) {
    if (eventSource.readyState \=== EventSource.CLOSED) {
        console.log("Connection was closed");
    }
};

2.  Connection Management

// Clean up when done
function closeConnection() {
    eventSource.close();
}

3.  Reconnection Strategy

let retryAttempts \= 0;
const maxRetries \= 5;

eventSource.onclose \= function() {
    if (retryAttempts < maxRetries) {
        setTimeout(() \=\> {
            // Reconnect logic
            retryAttempts++;
        }, 1000 \* retryAttempts);
    }
};

Real-World Example: ChatGPT's Implementation
--------------------------------------------

Modern Language Learning Models (LLMs) utilize Server-Sent Events (SSE) for streaming responses. Let's explore how these implementations work and what makes them unique.

The General Pattern
-------------------

All major LLM providers implement streaming using a common pattern:

*   Return `content-type: text/event-stream` header
*   Stream data blocks separated by `\r\n\r\n`
*   Each block contains a `data: JSON` line

### Important Note

While SSE typically works with the browser's EventSource API, LLM implementations can't use this directly because:

*   EventSource only supports GET requests
*   LLM APIs require POST requests

OpenAI Implementation
---------------------

### Basic Request Structure

curl https://api.openai.com/v1/chat/completions \\
  \-H "Content-Type: application/json" \\
  \-H "Authorization: Bearer $OPENAI\_API\_KEY" \\
  \-d '{
    "model": "gpt-4o-mini",
    "messages": \[{"role": "user", "content": "Hello, world?"}\],
    "stream": true,
    "stream\_options": {
      "include\_usage": true
    }
  }'

### Response Format

Each chunk follows this structure:

"data":{
   "id":"chatcmpl-AiT7GQk8zzYSC0Q8UT1pzyRzwxBCN",
   "object":"chat.completion.chunk",
   "created":1735161718,
   "model":"gpt-4o-mini-2024-07-18",
   "system\_fingerprint":"fp\_0aa8d3e20b",
   "choices":\[
      {
         "index":0,
         "delta":{
            "content":"!"
         },
         "logprobs":null,
         "finish\_reason":null
      }
   \],
   "usage":null
}

"data":{
   "id":"chatcmpl-AiT7GQk8zzYSC0Q8UT1pzyRzwxBCN",
   "object":"chat.completion.chunk",
   "created":1735161718,
   "model":"gpt-4o-mini-2024-07-18",
   "system\_fingerprint":"fp\_0aa8d3e20b",
   "choices":\[
      {
         "index":0,
         "delta":{
            
         },
         "logprobs":null,
         "finish\_reason":"stop"
      }
   \],
   "usage":null
}

Key headers returned by OpenAI:

HTTP/2 200
date: Wed, 25 Dec 2024 21:21:59 GMT
content-type: text/event-stream; charset=utf-8
access-control-expose-headers: X-Request-ID
openai-organization: user-esvzealexvl5nbzmxrismbwf
openai-processing-ms: 100
openai-version: 2020-10-01
x-ratelimit-limit-requests: 10000
x-ratelimit-limit-tokens: 200000
x-ratelimit-remaining-requests: 9999
x-ratelimit-remaining-tokens: 199978
x-ratelimit-reset-requests: 8.64s
x-ratelimit-reset-tokens: 6ms

Implementation Details
----------------------

### Stream Completion

The stream ends with:

### Usage Information

Final message includes token usage:

"data":{
   "id":"chatcmpl-AiT7GQk8zzYSC0Q8UT1pzyRzwxBCN",
   "object":"chat.completion.chunk",
   "created":1735161718,
   "model":"gpt-4o-mini-2024-07-18",
   "system\_fingerprint":"fp\_0aa8d3e20b",
   "choices":\[
      
   \],
   "usage":{
      "prompt\_tokens":11,
      "completion\_tokens":18,
      "total\_tokens":29,
      "prompt\_tokens\_details":{
         "cached\_tokens":0,
         "audio\_tokens":0
      },
      "completion\_tokens\_details":{
         "reasoning\_tokens":0,
         "audio\_tokens":0,
         "accepted\_prediction\_tokens":0,
         "rejected\_prediction\_tokens":0
      }
   }
}

Conclusion
----------

SSE provides an elegant solution for real-time, server-to-client communications. Its simplicity, efficiency, and integration with existing infrastructure make it an excellent choice for many applications. While WebSockets remain valuable for bidirectional communication, SSE offers a more focused and often more appropriate solution for one-way data streaming scenarios.

[#webdev](https://igorstechnoclub.com/blog/?q=webdev)

