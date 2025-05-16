---
layout: post
---
# GitHub - aipotheosis-labs/aci: ACI.dev is the open source platform that connects your AI agents to 600+ tool integrations with multi-tenant auth, granular permissions, and access through direct function calling or a unified MCP server.
- URL: [原文](https://github.com/aipotheosis-labs/aci)
- Added At: 2025-05-16 09:59:59
- [Link To Text](_posts/2025-05-16-aipotheosis-labs-aci_raw.md)

## TL;DR
ACI.dev是一个开源平台，旨在连接AI Agents与600多种工具集成。它提供多租户认证、细粒度权限控制，并通过统一的MCP服务器或直接函数调用进行访问。该项目解决了AI Agent在认证、工具发现和权限控制方面的挑战，适用于构建个人助理、研究代理和销售代理等多种应用场景。ACI.dev是框架和模型无关的，采用Apache 2.0许可证，鼓励社区参与共同发展。


## Summary
以下是根据您提供的文本生成的 Markdown 列表总结：

1.  **项目名称**：ACI.dev 是一个开源平台，旨在连接 AI agents 和 600 多个工具集成。

2.  **核心功能**：提供多租户认证、细粒度权限控制，并通过直接函数调用或统一的 MCP 服务器进行访问。

3.  **链接**：该项目在 GitHub 上的地址是 aipotheosis-labs/aci。

4.  **主要特性**：
    - **工具集成**：支持 600+ 预构建集成，快速连接常用服务和应用。
    - **访问方式**：灵活的访问方式，通过统一 MCP 服务器或轻量级 SDK 进行直接函数调用。
    - **多租户认证**：内置 OAuth 流程和密钥管理，适用于开发者和最终用户。
    - **可靠性**：自然语言权限边界和动态工具发现，提高 Agent 的可靠性。
    - **通用性**：框架和模型无关，适用于任何 LLM 框架和 Agent 架构。
    - **开源**：完全开源，采用 Apache 2.0 许可证。

5.  **解决的问题**：
    - **认证规模化**：安全地将多个用户连接到多个服务。
    - **发现无过载**：在不超出 LLM 上下文窗口的情况下，发现并使用正确的工具。
    - **自然语言权限**：使用人类可读的边界控制 Agent 的能力。
    - **一次构建，随处运行**：避免供应商锁定，采用开源、框架无关的方法。

6.  **应用场景**：
    - **个人助理聊天机器人**：构建可以搜索网络、管理日历、发送电子邮件、与 SaaS 工具交互的聊天机器人。
    - **研究代理**：在特定主题上进行研究，并将结果同步到其他应用程序（例如，Notion、Google Sheets）。
    - **外呼销售代理**：自动化潜在客户生成、电子邮件外联。

7.  **MCP Server**：如果需要使用 ACI.dev 构建的统一 MCP 服务器，可以参考 [aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)。

8.  **架构设计**：提供了平台架构图，展示了 ACI.dev 的整体设计。

9.  **社区参与**：鼓励加入 Discord 社区，共同塑造开源 AI 基础设施的未来。

10. **Demo视频**：提供了一个展示 ACI.dev 统一 MCP 服务器的演示视频链接。

11. **开发活动**：
    - **近期提交**：最近的提交包括统一使用 tanstack query 的 usepppconfig hooks 重构，更新 daytona app.json，以及修复 pre-commit 钩子配置等。
    - **代码结构**：代码库包含 `.github`、`backend` 和 `frontend` 目录，以及配置文件如 `.gitignore` 和 `.pre-commit-config.yaml`。

12. **贡献与协议**：
    - **CLA**：贡献者许可协议
    - **行为准则**：项目遵循行为准则。
    - **贡献指南**：有贡献指南，鼓励社区参与。
    - **安全策略**：提供安全策略，处理安全漏洞。

