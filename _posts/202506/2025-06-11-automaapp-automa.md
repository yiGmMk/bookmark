---
layout: post
---
# GitHub - AutomaApp/automa: A browser extension for automating your browser by connecting blocks
- URL: [原文](https://github.com/AutomaApp/automa)
- Added At: 2025-06-11 03:28:53
- [Link To Text](_posts/2025-06-11-automaapp-automa_raw.md)

## TL;DR
Automa是一款浏览器扩展，通过连接模块自动化浏览器操作，如表单填写、重复任务、数据抓取和定时任务。用户可在Chrome Web Store和Firefox Add-ons下载，并在Automa市场分享和下载工作流。它提供Chrome Extension Builder将工作流转换为独立扩展。项目基于AGPL或商业许可，并鼓励社区贡献。最新版本是v1.29.9。


## Summary
好的，这是对您提供的GitHub仓库信息的总结：

1.  **项目名称**：Automa

2.  **项目描述**：一个通过连接模块来自动化浏览器的浏览器扩展。

3.  **主要功能**：
    *   自动填写表单
    *   执行重复性任务
    *   截图
    *   抓取网站数据
    *   安排自动化任务执行时间

4.  **下载方式**：
    *   [Chrome Web Store](https://chrome.google.com/webstore/detail/automa/infppggnoaenmfagbfknfkancpbljcca)
    *   [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/automa/)

5.  **Automa市场**：
    *   提供分享和下载工作流的平台。
    *   链接：[https://www.automa.site/marketplace](https://www.automa.site/marketplace)

6.  **Automa CEB（Chrome Extension Builder）**：
    *   允许基于Automa工作流生成独立的Chrome扩展。
    *   文档链接：[https://docs.automa.site/extension-builder](https://docs.automa.site/extension-builder)

7.  **项目设置**：
    *   需要在`src/utils`目录下创建`getPassKey.js`文件，并导出一个返回任意值的函数。
    *   使用`pnpm install`安装依赖。

8.  **开发脚本**：
    *   `pnpm dev`: Chrome浏览器的开发模式，支持热重载。
    *   `pnpm build`: Chrome浏览器的生产环境构建。
    *   `pnpm build:zip`: 从构建文件夹创建一个zip文件。
    *   `pnpm dev:firefox`: Firefox浏览器的开发模式，支持热重载。
    *   `pnpm build:firefox`: Firefox浏览器的生产环境构建。
    *   `pnpm lint`: 检查和修复代码风格问题。

9.  **本地安装**：
    *   **Chrome**：
        1.  在Chrome中打开`chrome://extensions`页面。
        2.  启用"开发者模式"。
        3.  点击“加载已解压的扩展程序”，选择`automa/build`目录。
    *   **Firefox**：
        1.  在Firefox中打开`about:debugging#/runtime/this-firefox`页面。
        2.  点击“加载临时附加组件”按钮。
        3.  选择`automa/build`目录下的`manifest.json`文件。

10. **项目贡献者**：
    *   感谢提交问题、提供建议并帮助改进项目的贡献者。
    *   提供贡献者列表链接：[https://github.com/AutomaApp/automa/graphs/contributors](https://github.com/AutomaApp/automa/graphs/contributors)

11. **项目许可**：
    *   源代码在GNU Affero General Public License (AGPL)或[Automa Commercial License](https://www.automa.site/license/commercial/)下授权。
    *   详情请参阅[LICENSE.txt](https://github.com/AutomaApp/automa/blob/main/LICENSE.txt)文件。

12. **项目信息**：
    *   仓库地址：[https://github.com/AutomaApp/automa](https://github.com/AutomaApp/automa)
    *   项目网站：[https://extension.automa.site/](https://extension.automa.site/)
    *   相关话题：javascript, chrome-extension, workflow, automation, vue, firefox-extension, browser-extension, hacktoberfest, browser-automation

13. **项目数据**：
    *   Stars: 18.4k
    *   Watchers: 155
    *   Forks: 2k

14. **项目版本**：
    *   最新版本: v1.29.9 (发布于Mar 26, 2025)
    *   项目版本列表: [https://github.com/AutomaApp/automa/releases](https://github.com/AutomaApp/automa/releases)
15. **编程语言占比**：
    *   Vue: 57.3%
    *   JavaScript: 42.1%
    *   其他: 0.6%

