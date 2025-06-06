---
layout: post
---
# What is NLWeb?
- URL: [原文](https://glama.ai/blog/2025-06-01-what-is-nlweb)
- Added At: 2025-06-06 02:01:28
- [Link To Text](_posts/2025-06-06-what-is-nlweb_raw.md)

## TL;DR
NLWeb是由微软开源的协议，旨在通过利用Schema.org结构化数据和模型上下文协议(MCP)，为网站添加对话式AI接口。它通过多个LLM调用来处理查询，提供更精确的答案，并解决传统搜索的不足。虽然快速原型易于搭建，但大规模生产部署，优化成本以及维护数据新鲜度等方面仍面临挑战。对于已有结构化数据并寻求对话式搜索和AI代理访问的用户，NLWeb值得关注。


## Summary
1.  **NLWeb定义**: Microsoft开源的NLWeb是一种为网站添加对话式接口的协议，利用Schema.org结构化数据并支持MCP（模型上下文协议），促进人机和机机通信。
    *   **关键理念**: 将任何网站转变为人类和AI agent都能自然查询的对话式界面。

2.  **问题解决**: NLWeb旨在解决当前网站结构化数据缺乏标准AI访问方式的问题，并改进传统搜索在上下文感知和多轮查询方面的不足。
    *   **类比**: 类似于RSS对内容聚合的贡献，NLWeb为AI交互提供了一个标准协议。
    *   **核心优势**: 利用LLM对Schema.org的理解，快速创建对话式接口。

3.  **工作原理**: NLWeb采用双组件系统和查询处理流程。
    *   **双组件系统**:
        - **协议层**: REST API ( `/ask` endpoint) 和 MCP server (`/mcp` endpoint)，接受自然语言查询并返回 Schema.org JSON 响应。
        - **实现层**: 参考实现，编排多个LLM调用以进行查询处理。
    *   **查询处理流程**:
        User Query → Parallel Pre-processing → Vector Retrieval → LLM Ranking → Response (包含 Relevancy Check, Decontextualization, Memory Detection) → Fast Track Path
    *   **LLM调用**: 单个查询可能触发50+个定向LLM调用，用于查询去语境化、相关性评分、结果排序等。
    *   **快速通道优化**: 在预处理期间并行启动检索，但结果会阻塞直到完成相关性检查。

4.  **多LLM调用**: NLWeb将查询分解为多个小型、具体的LLM调用，而非一个大型提示。
    *   **示例问题**:
        - "这个查询是关于菜谱的吗？"
        - "它是否引用了之前提到的内容？"
        - "用户是否要求记住饮食偏好？"
        - "这个特定结果的相关性如何？"
    *   **主要优点**:
        -   **无幻觉**: 结果仅来自实际数据库。
        -   **更高精度**: 每个LLM调用都有一个清晰的任务可以做好。

5.  **快速上手**: Microsoft提供了一个快速入门指南，用于设置带有Behind The Tech RSS feed的NLWeb服务器。
    *   **步骤示例**:
        ```bash
        git clone https://github.com/microsoft/NLWeb
        cd NLWeb
        python -m venv myenv
        source myenv/bin/activate
        cd code
        pip install -r requirements.txt
        # Configure (copy .env.template → .env, update API keys)
        # Load data
        python -m tools.db_load https://feeds.libsyn.com/121695/rss Behind-the-Tech
        # Run
        python app-file.py
        ```
    *   **验证**: 访问 `localhost:8000` 检查 NLWeb server 是否工作。
    *   **CLI工具**: 仓库包含一个CLI工具来简化配置、测试和执行，但作者未能成功使用。

6.  **Glama NLWeb服务器**: 作者构建了一个简单的NLWeb服务器，可以使用它来查询MCP服务器目录。
    *   **示例请求**:
        ```bash
        curl -X POST https://glama.ai/nlweb/ask \
        -H "Content-Type: application/json" \
        -d '{"query": "MCP servers for working with GitHub"}'
        ```
    *   **其他功能**: 能够继续对话，总结或生成结果。
    *   **实施便利**: 已经存在MCP服务器的嵌入和向量存储，并且有调用LLM的方式。

7.  **REST API**: NLWeb在`/ask`和`/mcp`端点支持两个API，参数基本相同。
    *   **/mcp端点**: 返回MCP客户端可以使用的格式，并支持核心MCP方法。
    *   **/ask端点**:
        -   **参数**:
            -   `query`: 自然语言问题
            -   `site`: 限定到特定数据子集
            -   `prev`: 逗号分隔的先前查询
            -   `decontextualized_query`: 如果提供，则跳过去语境化
            -   `streaming`: 启用SSE流式传输
            -   `query_id`: 跟踪对话
            -   `mode`: `list`，`summarize`或`generate`

8.  **MCP集成**: NLWeb默认包含一个MCP服务器，可以配置Claude for Desktop与之通信。
    *   **配置步骤**: 将相关配置添加到`claude_desktop_config.json`。

9.  **实施现实**: 拥有Schema.org markup或RSS feed可以快速运行一个基本原型。
    *   **容易实现的**:
        -   加载RSS feeds或Schema.org数据
        -   使用提供的提示的基本搜索功能
        -   使用Qdrant进行本地开发
    *   **需要更多努力的**:
        -   大规模生产部署
        -   优化每个查询的50多个LLM调用
        -   针对您的域的自定义提示工程
        -   维护向量存储和实时数据之间的数据新鲜度
    *   **成本考量**: 需要考虑LLM调用的成本。

10. **是否应该关注**:
    *   **应该**: 已经有结构化数据，需要超越关键词的对话式搜索，需要通过MCP进行程序化AI代理访问，以及可以试验早期阶段的技术。
    *   **不应该**: 需要经过实战检验的生产代码，无法承担高昂的LLM API成本，内容结构不佳，以及期望即插即用的简易性。

11. **总结**: NLWeb作为战略方向比作为当前技术更有意义，由Schema.org、RSS和RDF的创建者R.V. Guha开发，证明了其可行性，但从原型到生产仍需努力。


