---
layout: post
---
Title: Hugo使用Shortcode插入bilibili、Youtube视频

URL Source: https://blog.lufei.de/p/hugo%E4%BD%BF%E7%94%A8shortcode%E6%8F%92%E5%85%A5bilibiliyoutube%E8%A7%86%E9%A2%91/

Published Time: 2023-07-29T15:18:42+00:00

Markdown Content:
前言
--

使用个人博客也有一年多的时间，这一年多的时候踩了很多坑，也学到了很多知识。 这里分享一个系列教程：从零开始搭建个人博客，把我的经验分享在这里。

Shortcodes 是什么
--------------

shortcode 可以理解为 **HTML 模版**，可以很方便的支持 markdown 里面写一行规定格式的代码，能用 shortcode 里面的模版替换成对应的 HTML 文件，然后就把这段 HTML 代码添加到编译之后的 HTML 文件中。

`Hugo shortcode`

`//注：去掉@，我这里是为了防止自动编译`

`{@{< name parameter1 parameter2 >}}`

然后在你的`主题`的 `layouts/shortcodes` 会自动找 名字为 name.html 的文件，就把参数的值替换到 html 中，得到一个最终的 html 信息。

shortcode 可以很方便的做复用，可以让你在每个 markdown 文件里面添加很少的内容，通常是一行代码，就能生成一个通用的 HTML 片段。

使用 Shortcode，我们就能很方便的通过一行简单的代码来插入 B 站或者 Youtube 视频。

插入视频
----

我们就教大家怎么在 Hugo 中嵌入 Bilibili 视频和 Youtube 视频，这样当别人访问你的个人博客网站的时候，可以直接点击播放你插入的视频，还可以自动跳转到你的自媒体平台播放视频，来给你的自媒体平台引流。

### 1. 嵌入 Bilibili 视频

在 hugo 网站目录你使用的主题目录下 `themes/{your theme name}/layouts/shortcodes` 中创建 bilibili.html 文件。

```
<!DOCTYPE HTML>
<html>

  <head>
    <!-- style 样式 是为了让网页上的视频框按比例显示而非固定的大小 -->
    <style type="text/css">
      .aspect-ratio {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 75%;
      }

      .aspect-ratio iframe {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
      }
    </style>
  </head>

  <body>
    <div class="aspect-ratio">
      <iframe
              src="https://player.bilibili.com/player.html?bvid={{.Get 0 }}&page={{ if .Get 1 }}{{.Get 1}}{{ else }}1&high_quality=1&danmaku=0{{end}}"
              scrolling="no" 
              border="0" 
              frameborder="no" 
              framespacing="0" 
              allowfullscreen="true"
              >
      </iframe>
      <!-- src 中的 &high_quality=1&danmaku=0 设定了高清程度并默认屏蔽弹幕 -->
    </div>
  </body>

</html>
```

然后在你的 bilibli 的连接上找到 BV 号。 比如我的视频链接是： [https://www.bilibili.com/video/BV1n8411K7zr/?vd_source=adec61d169fe18e7682f66c984380921](https://www.bilibili.com/video/BV1n8411K7zr/?vd_source=adec61d169fe18e7682f66c984380921)

那么 BV 号就是：`BV1n8411K7zr`

在你的 markdown 文件里面添加这么一行

这样就能展示你的 B 站视频了:

点击`去Bilibili观看`或者`吐槽`会自动跳转到 b 站对应的视频链接继续观看，非常方便。

2. 嵌入 Youtube 视频
----------------

Hugo 是自带 Youtube 视频的插入的，所以我们甚至不需要自己添加 shortcode 模板。

找到你的视频链接：

`https://www.youtube.com/watch?v=kDQJF6Ngsi0` 你只需要取到 v=xxxx 里面的 xxxx 内容 也就是你只需要写

就会自动匹配 Hugo 自带的 `shortcode` 模板，嵌入你的 youtube 视频。

如果你不想用 hugo 自带的 shortcode 模板，或者它无法正常插入视频，那么同样的方式在你使用的主题目录下 `themes/{your theme name}/layouts/shortcodes` 中创建 youtube.html 文件。

```
<style>
    .meta-media {
      position: relative;
      margin-bottom: 30px;
      display: flex;
      width: 100%;
      height: 0;
      padding-bottom: 75%;
    }
    .video {
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0;
      top: 0;
    }
    </style>
    <div class="meta-media">
    <iframe src="https://www.youtube.com/embed/{{ .Get 0 }}" frameborder="no" scrolling="yes" allowfullscreen="allowfullscreen" high_quality="1" framespacing="1" class="video" >
    </iframe>
    </div>
```

看一下效果：

结论
--

`shortcodes` 是不是很方便？让你在博客里面只需要写上一行代码就可以自动链接到 B 站或者 Youtube，可以非常方便的引流。赶快在你的个人博客加入 shortcodes 添加 B 站和 Youtube 视频吧。能大大提高你的 B 站和 Youtube 视频的站外曝光率。

