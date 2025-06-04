---
layout: post
---
# Hugo使用Shortcode插入bilibili、Youtube视频
- URL: [原文](https://blog.lufei.de/p/hugo%E4%BD%BF%E7%94%A8shortcode%E6%8F%92%E5%85%A5bilibiliyoutube%E8%A7%86%E9%A2%91/)
- Added At: 2025-06-04 15:55:44
- [Link To Text](_posts/2025-06-04-hugo使用shortcode插入bilibili、youtube视频_raw.md)

## TL;DR
本文介绍了如何在 Hugo 博客中使用 Shortcode 嵌入 Bilibili 和 Youtube 视频。通过创建自定义的 `bilibili.html` 和 `youtube.html` 文件，并在其中添加相应的 HTML 代码，可以在 Markdown 文件中方便地使用 Shortcode 插入视频，实现站外引流。文章详细说明了提取视频 ID 和 BV 号的方法，并提供了相应的 HTML 代码示例。 Hugo 自带 Youtube Shortcode，也可以自定义。


## Summary
这是对你提供的关于 Hugo 中使用 Shortcode 插入 Bilibili 和 Youtube 视频的教程文章的详细总结：

1.  **简介**：
    *   分享搭建个人博客的经验教程，重点介绍 Shortcode 的使用。

2.  **Shortcode定义**：
    *   本质：HTML 模板。
    *   功能：替换 Markdown 中的代码，插入 HTML 代码片段。
    *   位置：主题的 `layouts/shortcodes` 目录。
    *   用法：通过预定义格式的代码，调用对应的 HTML 模板，并传递参数。
    *   优点：简化 Markdown 文件内容，实现 HTML 代码复用。

3.  **视频嵌入**：
    *   目标：方便地在 Hugo 博客中嵌入 Bilibili 和 Youtube 视频，实现引流。

4.  **Bilibili 视频嵌入**：
    *   步骤：
        1.  创建 `bilibili.html` 文件：在 `themes/{your theme name}/layouts/shortcodes` 目录下创建。
        2.  添加 HTML 代码：将提供的 HTML 代码复制到 `bilibili.html` 文件中。代码包含样式定义和 iframe 标签，用于显示视频。
        3.  提取 BV 号：从 Bilibili 视频链接中提取 BV 号（例如 `BV1n8411K7zr`）。
        4.  Markdown 中使用 Shortcode：在 Markdown 文件中使用 `{{< bilibili BV1n8411K7zr >}}` 这样的 Shortcode 引用视频。
    *   HTML 代码功能：
        *   自适应比例：通过 CSS 样式，使视频框按比例显示。
        *   高清和弹幕设置：在 `iframe` 的 `src` 属性中，设定了高清程度 (`high_quality=1`) 并默认屏蔽弹幕 (`danmaku=0`)。

5.  **Youtube 视频嵌入**：
    *   方法一（使用 Hugo 自带 Shortcode）：
        1.  提取视频 ID：从 Youtube 视频链接中提取视频 ID（`v=xxxx` 中的 `xxxx` 部分）。
        2.  Markdown 中使用 Shortcode：在 Markdown 文件中使用 `{{< youtube kDQJF6Ngsi0 >}}` 这样的 Shortcode 引用视频。
    *   方法二（自定义 Shortcode，可选）：
        1.  创建 `youtube.html` 文件：在 `themes/{your theme name}/layouts/shortcodes` 目录下创建。
        2.  添加 HTML 代码：将提供的 HTML 代码复制到 `youtube.html` 文件中。
        3.  Markdown 中使用 Shortcode：在 Markdown 文件中使用 `{{< youtube kDQJF6Ngsi0 >}}` 这样的 Shortcode 引用视频。

6.  **结论**：
    *   Shortcode 方便快捷，一行代码即可插入 Bilibili 或 Youtube 视频。
    *   通过嵌入视频，增加 B 站和 Youtube 视频的站外曝光率，实现引流。

