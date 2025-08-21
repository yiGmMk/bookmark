---
layout: post
---
# Claude Code Best Practices
- URL: [原文](https://www.anthropic.com/engineering/claude-code-best-practices)
- Added At: 2025-08-21 08:31:24
- [Link To Text](_posts/2025-08-21-claude-code-best-practices_raw.md)

## TL;DR
Claude Code是Anthropic开发的命令行工具，旨在将Claude模型集成到编码工作流程中。通过定制设置、扩展工具、利用常用工作流程，并结合优化技巧，用户可以更高效地利用Claude Code进行代码探索、规划、编写、测试、提交，甚至进行代码库问答和Git/GitHub交互。无头模式和多Claude工作流程进一步提升了自动化和并行处理能力，建议用户根据自身需求进行实验和调整，以实现最佳效果。


## Summary
好的，这是对你提供的 Claude Code 最佳实践文章的 Markdown 列表式详细总结：

1.  **Claude Code 简介**: Claude Code 是 Anthropic 开发的命令行工具，用于 agentic coding，方便工程师和研究人员将 Claude 集成到他们的编码工作流程中。

2.  **设计理念**: Claude Code 保持低级别和非主观性，提供接近原始模型的访问，不强制特定工作流程，从而实现灵活、可定制、可脚本化和安全。

3.  **最佳实践**: 文章概述了 Anthropic 内部团队和外部工程师在使用 Claude Code 过程中发现的有效模式，强调实验和个性化。

4.  **定制设置**:

    *   **`CLAUDE.md` 文件**:
        *   **作用**: Claude Code 启动会话时自动加载的特殊文件，用于记录常用 bash 命令、核心文件、代码风格指南、测试说明、仓库规范、开发环境设置等信息。
        *   **位置**: 可以放置在仓库根目录、父目录、子目录或用户主目录下。
        *   **用途**: 通过 `/init` 命令自动生成，通过 `#` 键添加指令，并定期优化其内容。

    *   **允许的工具列表**:
        *   **目的**: 用于控制 Claude Code 可以执行的操作，默认采用保守策略以保证安全。
        *   **管理方式**: 通过对话提示选择“始终允许”、使用 `/permissions` 命令、手动编辑 `.claude/settings.json` 或使用 `--allowedTools` 命令行参数。

    *   **GitHub CLI**: 如果使用 GitHub，建议安装 `gh` CLI，以便 Claude 可以更方便地与 GitHub 交互。

5.  **扩展工具**:

    *   **Bash 工具**: Claude Code 继承 bash 环境，可以通过提供工具名称和用法示例、运行 `--help` 命令以及在 `CLAUDE.md` 中记录来让 Claude 使用自定义 bash 工具。

    *   **MCP**: Claude Code 既是 MCP 服务器又是客户端，可以通过项目配置、全局配置或 `.mcp.json` 文件访问 MCP 服务器上的工具。
        *  **调试**: 使用 `--mcp-debug` 标志有助于识别 MCP 配置问题。

    *   **自定义斜杠命令**: 将常用的 prompt 模板存储在 `.claude/commands` 文件夹中，通过 `/` 命令菜单访问，支持使用 `$ARGUMENTS` 传递参数。

6.  **常用工作流程**:

    *   **探索、计划、编码、提交**:
        1.  要求 Claude 读取相关文件、图片或 URL，但不要立即编写代码。可以使用子代理验证细节。
        2.  要求 Claude 制定解决方案计划，使用 "think" 等词语触发扩展思考模式。
        3.  要求 Claude 实现代码，并验证其解决方案的合理性。
        4.  要求 Claude 提交代码并创建 pull request。

    *   **编写测试、提交；编码、迭代、提交**:
        1.  要求 Claude 基于预期输入/输出对编写测试。
        2.  要求 Claude 运行测试并确认测试失败。
        3.  要求 Claude 提交测试。
        4.  要求 Claude 编写通过测试的代码，且不修改测试。可以使用子代理验证实现是否过度拟合测试。
        5.  要求 Claude 提交代码。

    *   **编写代码、截图结果、迭代**:
        1.  提供 Claude 截取浏览器截图的方法。
        2.  提供视觉 mock。
        3.  要求 Claude 实现设计，截取结果截图，并迭代直到结果与 mock 匹配。
        4.  要求 Claude 提交代码。

    *   **安全 YOLO 模式**: 使用 `claude --dangerously-skip-permissions` 绕过权限检查，适用于修复 lint 错误或生成样板代码等工作流程，建议在没有互联网访问的容器中使用，以降低风险。

    *   **代码库问答**: 使用 Claude Code 学习和探索新的代码库，询问有关代码库的各种问题。

    *   **与 Git 交互**: Claude 可以有效地处理许多 Git 操作，如搜索 Git 历史、编写提交消息、处理复杂的 Git 操作。

    *   **与 GitHub 交互**: Claude Code 可以管理许多 GitHub 交互，如创建 pull request、实现代码审查意见的快速解决、修复失败的构建或 linter 警告、对未解决的问题进行分类和分类。

    *   **使用 Jupyter notebook**: 使用 Claude Code 来读取和编写 Jupyter notebook。 特别是告诉它使笔记本或其数据可视化“美观”往往有助于提醒它正在为人类的观看体验进行优化。

7.  **优化工作流程**:

    *   **指令明确**: 越具体的指令，Claude Code 的成功率越高。
    *   **提供图像**: 通过截图、拖放或提供文件路径，Claude 可以更好地理解 UI 开发的设计 mock 和分析调试的视觉图表。
    *   **提及文件**: 使用 tab 补全快速引用仓库中的文件或文件夹，帮助 Claude 找到或更新正确的资源。
    *   **提供 URL**: 粘贴 URL，让 Claude 获取和读取网页内容。
    *   **及时纠正**: 积极参与并指导 Claude 的方法，在开始时彻底解释任务，或随时纠正 Claude 的方向。
    *   **使用 `/clear`**: 清除不相关的对话、文件内容和命令，保持上下文专注。
    *   **使用检查清单和草稿**: 对于大型任务，可以使用 Markdown 文件或 GitHub issue 作为检查清单和草稿。
    *   **传递数据**: 通过复制粘贴、管道输入、bash 命令、MCP 工具或自定义斜杠命令、读取文件或获取 URL 等方式向 Claude 提供数据。

8.  **无头模式**: 使用 `-p` 标志启用无头模式，用于自动化 CI、pre-commit 钩子、构建脚本等非交互式上下文。

    *   **问题分类**: 使用 Claude 检查新问题并分配标签。

    *   **作为 linter**: Claude 可以提供超越传统 linting 工具的主观代码审查，识别拼写错误、过时的注释、误导性的函数或变量名称等问题。

9.  **多 Claude 工作流程**: 并行运行多个 Claude 实例以提高效率。

    *   **一个 Claude 编写代码，另一个 Claude 验证**: 分离上下文，使 Claude 专注于不同的任务。

    *   **多个代码库副本**: 创建 3-4 个 Git 代码库副本，在单独的终端标签中打开，并在每个文件夹中启动 Claude，执行不同的任务。

    *   **使用 git worktrees**: 允许您从同一存储库将多个分支签出到单独的目录中。

    *   **与自定义 harness 配合使用无头模式**: 通过 `--verbose` 标志调试 Claude 调用，建议在生产环境中关闭详细模式以获得更清晰的输出。
        *   **Fanning out**: 处理大型迁移或分析。
        *   **Pipelining**: 将 Claude 集成到现有的数据/处理管道中。

