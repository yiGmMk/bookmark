# LLM x 书签收藏：摘要 & 全文索引
- URL: [原文](https://nekonull.me/posts/llm_x_bookmark/)
- Added At: 2024-12-16 08:02:19
- [Link To Text](_posts/2024-12-16-llm-x-书签收藏：摘要-&-全文索引---nekonull's-garden_raw.md)

## TL;DR
作者使用名为 osmos::memo 的书签插件将收藏记录到一个公开的 Github 存储库中。然而，目前的书签收藏流程中存在一些问题，如书签指向的 URL 可能不再存在、记录项信息不全和书签内容难以快速查找。为了解决这些问题，作者建立了一个新的存储库 bookmark-summary，包含新增书签的 Markdown 格式全文、列表摘要和一句话总结。通过 Github Actions 联动，实现了自动保存 URL 到 Wayback Machine、获取网址的 Markdown 全文、生成列表摘要和一句话总结等功能。

## Summary
**背景**
--------

网上冲浪时，经常会遇到一些有趣的文章或者网站，让人有收藏起来以备后用的冲动。然而一个人收藏未免有些太孤单了，因此自从 2021 年 5 月以来，作者一直在使用一个名为 [osmos::memo](https://github.com/osmoscraft/osmosmemo) 的书签插件，将收藏直接记录到一个公开的 [Github 存储库](https://github.com/jerrylususu/bookmark-collection)。

**问题**
------

然而目前的书签收藏流程中，依然会存在一些问题。

1.  **书签指向的 URL 可能不再存在**：导致成为悬空的死链接
2.  **记录项信息不全**：目前的记录项只有书签的 URL、标题和可选的标签，导致查找的时候如果对关键词记忆不清楚，很有可能找不到
3.  **书签内容难以快速查找**：书签里一大部分是长文章，时间一久很有可能忘记内容，如果只是临时找些东西，通读一次又略微有些费时费事，导致查找&引用效率下降

**解决**
------

为了解决这些问题，作者建立了一个新的存储库 [bookmark-summary](https://github.com/jerrylususu/bookmark-summary)。这个存储库可以视为现有书签存储库的辅助数据，其中包含了新增书签的 Markdown 格式全文、列表摘要、一句话总结，和现有存储库之间通过 Github Actions 联动。

**工作原理**
------------

1.  **新增书签**：作者通过书签插件，在现有的书签存储库中新增了一个条目
2.  **触发 Github Actions**：代码提交到主干，触发名为 `summarize` 的 Github Actions
3.  **执行 process_changes.py**：Github Actions 执行，首先 checkout 书签存储库和摘要存储库，然后执行 [process\_changes.py](https://github.com/jerrylususu/bookmark-summary/blob/main/process_changes.py)
    1.  **解析书签 README.md 文件**：找到最近新增的条目标题和 URL
    2.  **保存 URL 到 Wayback Machine**：将 URL 保存到 Wayback Machine
    3.  **获取网址的 Markdown 全文**：使用 [jina reader](https://jina.ai/reader/) API 获取网址的 Markdown 全文，并保存到 `YYYYMM/{title}_raw.md`
    4.  **生成列表摘要**：使用 LLM 生成列表摘要
    5.  **生成一句话总结**：使用 LLM 生成一句话总结
    6.  **保存列表摘要和一句话总结**：将列表摘要和一句话总结保存到 `YYYYMM/{title}.md`
    7.  **更新摘要存储库的 README.md**：增加到摘要文件的链接

**未来**
------

最后是一些已知问题，以及未来可能的优化方向。

1.  **列表摘要质量**：可能是 prompt 的问题，列表摘要倾向于每个大点下面只列两个小点，且没有充分合并需要合并的论点
2.  **数据结构化**：目前摘要存储库下有个简单的 data.json，但是核心的摘要和全文内容依然是 Markdown 存储的，而不是 JSON 这类程序友好的结构化存储
3.  **代码整理和重构**：目前所有逻辑都混在一个大的 Python 文件里，修改和测试起来都很烦人
4.  **向量搜索**：目前虽然原文和摘要都存下来了，搜索却还是只能靠基本的文本匹配
5.  **自动生成每周周报**：可以考虑每周新增的书签+原文+摘要全部往 LLM 扔，自动生成一个每周摘要
6.  **改用更现代的工具链**：例如 uv，以及把依赖写在 Python 代码头部

**我也想要**
------------

可以参考以下步骤，在自己的 Github 账户下部署一套类似的系统。

1.  **初始化书签存储库**：参考 [osmos::memo](https://github.com/osmoscraft/osmosmemo) 的指引，初始化书签存储库
2.  **新建摘要存储库**：新建一个摘要存储库，并在其中添加一个空的 README.md 文件
3.  **添加 process_changes.py**：将 [process\_changes.py](https://github.com/jerrylususu/bookmark-summary/blob/main/process_changes.py) 添加到摘要存储库
4.  **配置 Github Actions**：回到书签存储库，将 [bookmark\_summary.yml](https://github.com/jerrylususu/bookmark-collection/blob/main/.github/workflows/bookmark_summary.yml) 添加到 `.github/workflows/bookmark_summary.yml`
5.  **新建 PAT**：新建一个 PAT（Personal Access Token）
6.  **添加密钥到环境变量**：添加密钥到环境变量
