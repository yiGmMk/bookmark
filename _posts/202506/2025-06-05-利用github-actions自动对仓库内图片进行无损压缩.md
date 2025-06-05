---
layout: post
---
# 利用GitHub Actions自动对仓库内图片进行无损压缩
- URL: [原文](https://wiki.eryajf.net/pages/dbee9e/)
- Added At: 2025-06-05 01:54:19
- [Link To Text](_posts/2025-06-05-利用github-actions自动对仓库内图片进行无损压缩_raw.md)

## TL;DR
二丫讲梵的文章介绍了如何利用GitHub Actions和`calibreapp/image-actions`自动无损压缩仓库中的图片。通过在`.github/workflows/images.yml`中配置Actions，可以在push到指定分支时自动压缩图片，并创建Pull Request。实践表明，该方法能在保证清晰度的情况下大幅减小图片体积，尤其适用于图片较多的仓库。


## Summary
好的，这是对您提供的文本的详细总结：

1.  **文章标题**：利用GitHub Actions自动对仓库内图片进行无损压缩

2.  **文章来源**：二丫讲梵的个人Wiki，URL为：https://wiki.eryajf.net/pages/dbee9e/

3.  **发布时间**：2022年8月1日

4.  **文章概要**：
    - **问题背景**：维护的项目`awesome-github-profile-readme-chinese`通过截图方式存放个人主页，截图文件较大。
    - **解决方案**：利用GitHub Actions自动扫描并无损压缩仓库中的图片，减小仓库体积。

5.  **使用的Action**：
    -  **名称**：`image-actions`
    -  **作者**：`calibreapp`
    -  **链接**：[https://github.com/calibreapp/image-actions](https://github.com/calibreapp/image-actions)

6.  **配置步骤**：
    -  **创建配置文件**：在`.github/workflows/images.yml`添加配置。
    -  **配置文件内容**：给出了YAML配置示例，包含触发条件（push到main分支，指定图片类型），运行环境（ubuntu-latest），压缩步骤和创建Pull Request步骤。
    -  **配置示例关键参数**：
       - `githubToken`: `${{ secrets.GITHUB_TOKEN }}`，操作当前仓库使用，无需更改。
       - `compressOnly`: `true`，仅压缩图片。
       - `jpegQuality`, `pngQuality`, `webpQuality`:  图片质量参数，配置为"60"。
       - `jpegProgressive`: `false`，是否使用渐进式JPEG。

7.  **权限问题**：
    -  **问题描述**：压缩图片的动作需要commit权限，但通常token没有其他fork仓库的权限，无法直接处理PR中的图片。
    -  **官方建议**：
       -  其他开发者在主仓库check分支并PR。
       -  先同意PR，自动扫描压缩后再创建新的PR。

8.  **效果展示**：
    -  **压缩效果**：体积缩小80%的情况下，清晰度几乎一致。
    -  **操作方式**：Actions自动处理图片并提交到PR，可以查看diff。

9.  **总结**：适合存放图片较多的仓库，能在基本不影响清晰度的前提下大幅缩小图片体积。

10. **其他内容**：
    - **博客信息**：作者为“二丫讲梵”，提供了Github、邮箱、RSS订阅链接。
    - **版权信息**：主题为Vdoing，有Copyright信息和ICP备案号。
    - **网站模式**：提供跟随系统、浅色、深色、阅读模式切换。
    - **文章导航**：提供了文章的上一篇和下一篇链接，以及其他文章链接。
    - **打赏信息**：提供了微信和支付宝的打赏二维码。


