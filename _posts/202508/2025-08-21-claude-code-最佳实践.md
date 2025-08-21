---
layout: post
---
# Claude Code 最佳实践
- URL: [原文](https://ai.programnotes.cn/p/claude-code-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)
- Added At: 2025-08-21 10:04:39
- [Link To Text](_posts/2025-08-21-claude-code-最佳实践_raw.md)

## TL;DR
Anthropic 官方发布的 Claude Code 是一个底层且不固执己见的代理式编程工具，通过命令行高效利用 AI 编程。核心在于优化`CLAUDE.md`文件，有效管理工具权限，并结合具体指令、图像、URL等提升Claude Code的成功率。常用工作流包括探索-计划-编码-提交等。此外，还介绍了无头模式、代码库问答、git/GitHub 交互及 Jupyter Notebook 使用等。高级用法包括多 Claude 工作流。总而言之，文章旨在帮助开发者掌握 Claude Code 的实用技巧，提高开发效率。


## Summary
好的，这是对你提供的 Claude Code 最佳实践文章的 Markdown 列表式详细总结：

1.  **文章概述**：介绍了 Anthropic 官方发布的 Claude Code 使用最佳实践，帮助开发者高效利用 AI 进行编程。Claude Code 是一款用于代理式编码的命令行工具，旨在提供对模型的原生访问，同时保证安全。文章分享了在各种代码库、语言和环境中使用 Claude Code 的有效技巧和窍门。

2.  **核心理念**：Claude Code 被设计为底层且不固执己见，提供近乎原始的模型访问权限，不强加特定的工作流。

3.  **重要资源**：推荐阅读[claude.ai/code](claude.ai/code) 上的综合文档，涵盖所有功能、示例和高级技术。

4.  **设置自定义**：
    - **`CLAUDE.md` 文件**：
      - Claude 在开始对话时自动提取到上下文的特殊文件。
      - 存放常用 bash 命令、核心文件和实用函数、代码风格指南、测试说明、代码仓库礼仪、开发环境设置、项目特有警告等信息。
      - 建议保持简洁易读。
      - 可以放在仓库根目录、运行 `claude` 目录的父目录或子目录、用户主文件夹 (`~/.claude/CLAUDE.md`)。
      - 运行 `/init` 命令可自动生成 `CLAUDE.md` 文件。
    - **优化文件**：像优化其他提示一样，迭代优化 `CLAUDE.md` 文件内容，确保指令遵循效果。
    - **命令快捷**： 使用 `#` 键向 Claude 发出指令，它会自动将其合并到相关的 `CLAUDE.md`。
    - **强调指令**：在Anthropic，团队会使用提示改进器来运行 `CLAUDE.md` 文件，并经常调整指令（例如，用 “IMPORTANT” 或 “YOU MUST” 来强调）以提高遵循度。
    - **工具管理**：管理 Claude Code 允许的工具列表以保证安全性，通过以下方式：
      - 在会话期间出现提示时选择“始终允许”。
      - 使用 `/permissions` 命令添加或删除工具。
      - 手动编辑 `.claude/settings.json` 或 `~/.claude.json`。
      - 使用 `--allowedTools` CLI 标志。
    - **`gh` CLI**：如果使用 GitHub，建议安装 `gh` CLI，以便 Claude 与 GitHub 交互。

5.  **扩展工具集**：
    - **bash 工具**：
        - 继承 bash 环境，访问所有工具。
        - 告诉 Claude 工具名称和使用示例。
        - 告诉 Claude 运行 `--help` 查看工具文档。
        - 在 `CLAUDE.md` 中记录常用工具。
    - **MCP**：
        - 作为客户端连接到 MCP 服务器以访问工具。
        - 在项目配置、全局配置或 `.mcp.json` 文件中配置 MCP 服务器。
        - 使用 `--mcp-debug` 标志识别配置问题。
    - **斜杠命令**：
        - 在 `.claude/commands` 文件夹中存储提示模板，通过斜杠命令菜单访问。
        - 可包含特殊关键字 `$ARGUMENTS` 以传递参数。

6.  **常见工作流**：
    - **探索-计划-编码-提交**：
        1.  要求 Claude 阅读相关文件。
            - 考虑使用子代理来验证细节或调查它可能有的特定问题
        2.  要求 Claude 制定解决特定问题的方法计划。
           - 使用“思考（think）”这个词来触发扩展思考模式：“think” < “think hard” < “think harder” < “ultrathink”。
        3.  要求 Claude 用代码实现其解决方案。
        4.  要求 Claude 提交结果并创建一个 pull request。
    - **编写测试-提交；编码-迭代-提交**：
        1.  要求 Claude 根据预期的输入/输出对编写测试。
        2.  告诉 Claude 运行测试并确认它们失败。
        3.  当您对测试满意时，要求 Claude 提交测试。
        4.  要求 Claude 编写通过测试的代码，并指示它不要修改测试。
        5.  告诉 Claude 继续，直到所有测试都通过。
        6.  一旦您对更改感到满意，就要求 Claude 提交代码。
    - **编写代码-截图结果-迭代**：
        1.  为 Claude 提供一种截取浏览器屏幕截图的方法。
        2.  为 Claude 提供一个视觉模型。
        3.  要求 Claude 用代码实现设计，截取结果的屏幕截图，并进行迭代，直到其结果与模型匹配。
        4.  当您满意时，要求 Claude 提交。
    - **安全的“YOLO”模式**：
        - 使用 `claude --dangerously-skip-permissions` 绕过所有权限检查。
        - 建议在没有互联网访问的容器中使用，以降低风险。
    - **代码库问答**：
        - 使用 Claude Code 进行学习和探索。
        - 提出一般性问题，Claude 会搜索代码库找到答案。
    - **git 交互**：
        - 使用 Claude 处理 git 操作，如搜索历史记录、编写提交消息、处理 rebase 冲突等。
    - **GitHub 交互**：
        - 使用 Claude Code 管理 GitHub 交互，如创建 pull request、实施代码审查评论、修复构建失败等。
    - **Jupyter notebook**：
        - 使用 Claude Code 来读写 Jupyter notebook。
        - 要求 Claude 清理或美化 Jupyter notebook。

7.  **工作流优化**：
    - **指令具体**：
        - Claude Code 的成功率随着更具体的指令而显著提高。
    - **提供图像**：
        - 通过截图、拖放或文件路径向 Claude 提供图像。
    - **提及文件**：
        - 使用 Tab 键补全快速引用仓库中的文件或文件夹。
    - **提供URL**：
       - 将特定的 URL 与您的提示一起粘贴，供 Claude 获取和阅读。
    - **及早纠正**：
        - 使用“在编码前制定计划”、“中断 Claude”、“跳回历史记录”、“撤销更改”等工具进行路线修正。
    - **保持上下文专注**：
        - 使用 `/clear` 命令重置上下文窗口。
    - **清单草稿**：
        - 对于复杂任务，使用 Markdown 文件作为清单和工作草稿板。
    - **数据传递**：
        - 通过复制粘贴、管道传递、bash 命令/MCP 工具/斜杠命令、读取文件/获取 URL 等方式向 Claude 提供数据。

8.  **无头模式**：
    - 使用 `-p` 标志和提示启用无头模式，适用于 CI、预提交钩子、构建脚本等非交互式环境。
    - 使用 `--output-format stream-json` 进行流式 JSON 输出。
    - 可用于 issue 分流和作为 linter。

9.   **高级用法：多 Claude 工作流**：
    - **代码编写与验证分离**：
        - 使用一个 Claude 编写代码，另一个进行审查或测试。
    - **多个代码库副本**：
        - 创建多个 git 检出副本，在不同终端中以不同任务启动 Claude。
    - **Git Worktrees**：使用 git worktrees 管理多个会话
    - **无头模式集成**：
        - 通过扇出或管道化方式，将 Claude Code 集成到更大的工作流中。

