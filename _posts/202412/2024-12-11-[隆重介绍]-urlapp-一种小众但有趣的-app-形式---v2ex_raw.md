---
layout: post
---
Title: [隆重介绍] urlapp-一种小众但有趣的 app 形式 - V2EX

URL Source: https://www.v2ex.com/t/1059349

Published Time: 2024-07-23T02:33:00Z

Markdown Content:
首页 注册 登录
V2EX = way to explore
V2EX 是一个关于分享和探索的地方
现在注册
已注册用户请  登录
爱意满满的作品展示区。
广告
V2EX  ›  分享创造
[隆重介绍] urlapp-一种小众但有趣的 app 形式
  3     meeop · 141 天前 · 3940 次点击
这是一个创建于 141 天前的主题，其中的信息可能已经有所发展或是发生改变。

缘起： 去年我发了一个帖子，没想到获得热烈讨论，这个点子很有趣，而且有一定实用价值 https://www.v2ex.com/t/944717#reply149

经过更深入的思考，我发现这是一个相当不错的 app 形式，它不光具有优异的性能，还是一种分享代码的便利方式，从此发布 app 不再是一个高成本的事情了，你甚至可以一行代码作为一个 app 发布

什么是 urlapp

urlapp 是一种轻量开源 app 封装形式。
它使用 Data URL 规范（参考：Data URL 规范），封装一个单页面 html 应用为一个 url ，使用浏览器访问 url 可直接使用 app 。

如下链接是一个简单的 urlapp ，复制到浏览器地址栏运行

data:text/html;base64,PGh0bWwgY29udGVudGVkaXRhYmxlPmVkaXQgbWU8L2h0bWw+

这是一个网页记事本，它有很多一般 app 不具备的特性：

无需网络，永久可用
全平台支持，只依赖浏览器
易于分发
开源
轻量秒开
安全，浏览器对网页有严格限制
urlapp.org项目

urlapp 项目（urlapp.org）致力于提供一个使用，发布，推广，讨论，开发 urlapp 的平台。

urlapp 代码和数据永久开源（github 地址），欢迎收藏，点赞，讨论，分享

同时，github-discussions 板块(github-discussions 地址)也作为 urlapp 的讨论，发布，点评论坛，任何关于 urlapp.org 和 urlapp 的问题可以在这里讨论

urlapp.org还意图实现为一个永久可用服务，无后端服务依赖纯静态化设计，数据和代码都开源分发，只要你打开并保持 urlapp ，它就永远存在于你的电脑不会下线。后续还计划通过 ipfs 等平台加固服务可用性

沟通讨论平台: discord | telegram | github-discussions

发布一组 urlapp,欢迎探索
小工具
html 文本编辑、文本编辑、html 转 urlApp 、二维码生成、二维码扫描、动态表单编辑 json 、在线 html 编辑渲染
游戏
2048 小游戏、纸牌、马里奥 1k 、俄罗斯方块
微应用
模拟桌面、番茄计时器、任务四象限、计算器
原型设计
Autumn 、可爱风 3D 飞机飞行

更多信息请访问urlapp.org，所有 urlapp 都是开箱即用的，同时欢迎发布你的 urlapp 。

第 1 条附言  ·  18 天前
更新进展：

https://genwebapp.com/

升级为支持 ai 编辑的 genwebapp 了，可以直接编辑，发布，并立即可用的 urlapp ，还支持 ai 编辑
39 条回复  •  2024-11-22 12:51:14 +08:00
		
    1
yKXSkKoR8I1RcxaS      141 天前
酷
		
    2
qwertyzzz      141 天前
和普通网页有什么区别
		
    3
meeop   
OP
   141 天前
@qwertyzzz
1 易于分享
你可以在论坛聊天窗口直接分享一个 app,而且打开即用,类似这样
https://www.v2ex.com/t/1056167?p=1#reply20
普通网页的话,要么你自己部署然后分享 url,要么你给别人分发一个文件或者下载链接

2 永久可用
网页需要依赖后台服务器,应该经常能遇到收藏的一些网页过一段时间就打不开了
urlapp 不会,它以源码形式分享,加入收藏夹,就永远都能用

3 超低的开发/部署/分发成本
普通网页你需要一个后台服务器,正规一点的话还需要 icp 备案,域名备案,买 vps,全套下来几万块钱+费时费力
对于单 html 能力范围的场景,如果直接拿 dataurl 分享,纯粹的 0 成本,如果拿 urlapp.org 分享,也就发个帖子的事

4 轻量秒开
网页是有网络交互的,最快的网页打开也有眼屎
urlapp 不会,加入收藏夹后打开只有 3ms 加载时间
		
    4
qwertyzzz      141 天前
@meeop 和别人把网站给你 你统一部署有什么区别
		
    5
shadowyue      141 天前
你这个像是 PWA 的更精简版本。
提个问题，你这个应用的形式，如何解决更新的问题。
一旦我收藏了，就没法更新了
		
    6
meeop   
OP
   141 天前
@qwertyzzz 我想解决的场景是轻量的单 html 应用的分发问题,前面说了,这个形式的 app 有普通网页无法替代的一些属性,那,相对于部署在 github pages 这类静态网站托管服务:

1 这里分发的是一个打开即用的 app,而不是更发散的网页,并且提供一个集中的分发,使用,搜索,评价,反馈平台
2 只要保存页面,这个 app 永远可用,托管网站做不到这点(作者也可能删除页面)
3 开发和维护成本更低,发个帖子的成本

如果说有人做一个关于网页/网站的聚合,评价,分享,发布,托管平台倒是也类似,但那是一个更复杂的场景,和轻量 html 应用场景不冲突
		
    7
yjfkk      141 天前
酷就够了，虽然没啥用。
		
    8
meeop   
OP
   141 天前    1
@shadowyue 我想了 3 个办法:
1 对于在 urlapp.org 上发布,你需要以发帖的形式在 github discussion 上发一个发布 app 帖子
这个帖子就是你的 urlapp 发布页面了,后续更新/评价/讨论都可以围绕这个帖子进行
后续更新也可以以同样的形式发帖,而 urlapp.org 会处理发布帖子,定期录入更新 urlapp
urlapp.org 上的 urlapp 永远是最新的
参考:https://urlapp.org/apps/doc2024072200003/howToPublish

2 可以直接联系作者,追更或者订阅

3 代码开源的,小修改可以自己动手(这一点几乎所有 app 都做不到)
		
    9
meeop   
OP
   141 天前    1
@shadowyue 比如你可以收藏 urlapp 的落地页,这个页面会保持最新,也是 urlapp.org 这个网站主要解决的问题
https://urlapp.org/detailPage?appId=app2024072200007
		
    10
qwertyzzz      141 天前
@meeop #6 感觉和那种别人做的工具类的网站区别不大呀。。就是这个可以下载是吧
		
    11
meeop   
OP
   141 天前
@qwertyzzz 相对工具类网站呢:
1 网站和 app 保持永久可用,好用的工具你收藏后就是你的,不会有一天没了

2 代码开源,app 有些细节想调整(比如 json 格式化加个粘贴自动格式化功能),工具站可不给你调整,你可以在源码基础上自己调整

3 他不止工具站啊,单 html 应用是一个 app,它还可以是游戏,动画,应用

4urlapp.org 还会提供在线使用,讨论,反馈,评价能力,会提供一些社区能力

5 就工具类应用而言,urlapp 不需要网络,打开非常快,几个毫秒级别
		
    12
ClarkAbe      140 天前
@qwertyzzz 可以保存在书签然后离线使用
		
    13
meeop   
OP
   140 天前
@qwertyzzz 举个例子,比如 json 格式化,下面这个链接会比任何其他 json 格式化工具加载迅速(完全感受不到加载时间)

data:text/html;base64,PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CjxtZXRhIGNoYXJzZXQ9IlVURi04Ij4KPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiPgo8dGl0bGU+SlNPTiBGb3JtYXR0ZXI8L3RpdGxlPgo8c3R5bGU+CiAgYm9keSwgaHRtbCB7CiAgICBoZWlnaHQ6IDEwMCU7CiAgICB3aWR0aDogMTAwdnc7CiAgICBtYXJnaW46IDA7CiAgICBkaXNwbGF5OiBmbGV4OwogICAgZm9udC1mYW1pbHk6IEFyaWFsLCBzYW5zLXNlcmlmOwogIH0KICB0ZXh0YXJlYSB7CiAgICB3aWR0aDogNTAlOwogICAgaGVpZ2h0OiAxMDAlOwogICAgYm94LXNpemluZzogYm9yZGVyLWJveDsgLyogRW5zdXJlcyBubyBvdmVyZmxvdyAqLwogICAgYm9yZGVyLXdpZHRoOiAxcHg7IC8qIFJlbW92ZXMgdGhlIGJvcmRlciAqLwogICAgb3V0bGluZTogbm9uZTsgLyogUmVtb3ZlcyB0aGUgb3V0bGluZSAqLwogICAgcmVzaXplOiBub25lOyAvKiBQcmV2ZW50IHJlc2l6aW5nICovCiAgICBwYWRkaW5nOiAxMHB4OyAvKiBBZGRzIHNvbWUgcGFkZGluZyBpbnNpZGUgdGhlIHRleHRhcmVhICovCiAgICBmb250LXNpemU6IDE2cHg7IC8qIEluY3JlYXNlcyBmb250IHNpemUgZm9yIGJldHRlciByZWFkYWJpbGl0eSAqLwogIH0KPC9zdHlsZT4KPC9oZWFkPgo8Ym9keT4KPHRleHRhcmVhIGlkPSJpbnB1dEpzb24iIHBsYWNlaG9sZGVyPSJQYXN0ZSBKU09OIGhlcmUiPjwvdGV4dGFyZWE+Cjx0ZXh0YXJlYSBpZD0ib3V0cHV0SnNvbiIgcGxhY2Vob2xkZXI9IkZvcm1hdHRlZCBKU09OIHdpbGwgYXBwZWFyIGhlcmUiIHJlYWRvbmx5PjwvdGV4dGFyZWE+Cgo8c2NyaXB0PgogIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdpbnB1dEpzb24nKS5hZGRFdmVudExpc3RlbmVyKCdpbnB1dCcsIGZ1bmN0aW9uKCkgewogICAgdmFyIGlucHV0ID0gdGhpcy52YWx1ZTsKICAgIHRyeSB7CiAgICAgIHZhciBvdXRwdXQgPSBKU09OLnN0cmluZ2lmeShKU09OLnBhcnNlKGlucHV0KSwgbnVsbCwgNCk7CiAgICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdvdXRwdXRKc29uJykudmFsdWUgPSBvdXRwdXQ7CiAgICB9IGNhdGNoIChlKSB7CiAgICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdvdXRwdXRKc29uJykudmFsdWUgPSAiRXJyb3I6ICIgKyBlLm1lc3NhZ2U7CiAgICB9CiAgfSk7Cjwvc2NyaXB0Pgo8L2JvZHk+CjwvaHRtbD4K
		
    14
meeop   
OP
   140 天前
@qwertyzzz 还有就是无广告,工具站为了盈利一定是要塞广告的,或者弹窗,或者占用 ui 面积
urlapp 可以有广告,但是是开源的,不爽你可以自己删掉广告
		
    15
adrianzhang      140 天前
感觉不错呀
		
    16
huajingkun1214      140 天前 via Android    1
我想到一个好玩的点, urlapp.org 能实现自举吗？
		
    17
meeop   
OP
   140 天前
@huajingkun1214 可以,项目构建后其实就只有一个 html+一个 js 文件,可以手动合并为一个 html 文件
只不过出于页面加载速度考虑我没这么干,实践上我验证过一个 100m 的 html 文件毫无问题
100M 按照 10k 一个 urlapp 可以容纳 1w 个 app 了,我估计永远都不会有这么多数据
		
    18
meeop   
OP
   140 天前
@huajingkun1214 这里有个例子，你可以在一个 urlapp 里访问 urlapp
https://urlapp.org/apps/app2024072200008/virtualWin
		
    19
body007      140 天前    1
之前有分享这个复制代码的地址，挺好使的。

data:text/html;base64,PGh0bWw+PGhlYWQ+CiAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCI+CiAgICA8bWV0YSBodHRwLWVxdWl2PSJYLVVBLUNvbXBhdGlibGUiIGNvbnRlbnQ9IklFPWVkZ2UiPgogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiPgogICAgPHRpdGxlPkRvY3VtZW50PC90aXRsZT4KICA8L2hlYWQ+CiAgPGJvZHk+CiAgICA8YnV0dG9uIGlkPSJidG4iPkNvcHkgVXJsPC9idXR0b24+CiAgICA8ZGl2IGlkPSJlZGl0b3ItYXJlYSIgY29udGVudGVkaXRhYmxlPSIiPjxkaXYgc3R5bGU9ImJhY2tncm91bmQtY29sb3I6IzJiMmIyYjtjb2xvcjojYTliN2M2Ij48cHJlIHN0eWxlPSJmb250LWZhbWlseTonbW9ub25va2knLG1vbm9zcGFjZTtmb250LXNpemU6MTguMHB0OyI+PHNwYW4gc3R5bGU9ImNvbG9yOiNjYzc4MzI7Ij5wYWNrYWdlIDwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6I2E3YzZhMjsiPm1haW48YnI+PC9zcGFuPjxzcGFuIHN0eWxlPSJjb2xvcjojYTdjNmEyOyI+PGJyPjwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6I2NjNzgzMjsiPmltcG9ydCA8L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiNlOGJhMzY7Ij4oPGJyPjwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6I2U4YmEzNjsiPiAgICA8L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiMzMGJlNDc7Ij4iZm10Ijxicj48L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiNlOGJhMzY7Ij4pPGJyPjwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6I2U4YmEzNjsiPjxicj48L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiNjYzc4MzI7Ij5mdW5jIDwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6I2ZmN2IwMDsiPm1haW48L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiNlOGJhMzY7Ij4oKSB7PGJyPjwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6I2U4YmEzNjsiPiAgICA8L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiNhN2M2YTI7Ij5mbXQ8L3NwYW4+LjxzcGFuIHN0eWxlPSJjb2xvcjojOGFmZjA3OyI+UHJpbnRsbjwvc3Bhbj48c3BhbiBzdHlsZT0iY29sb3I6IzU0YTg1NzsiPig8L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiMzMGJlNDc7Ij4iaGVsbG8iPC9zcGFuPjxzcGFuIHN0eWxlPSJjb2xvcjojNTRhODU3OyI+KTxicj48L3NwYW4+PHNwYW4gc3R5bGU9ImNvbG9yOiNlOGJhMzY7Ij59PGJyPjwvc3Bhbj48L3ByZT48L2Rpdj48L2Rpdj4KICAgIDxzdHlsZT4KICAgICAgI2VkaXRvci1hcmVhIHsKICAgICAgICB3aWR0aDogMTAwJTsKICAgICAgICBoZWlnaHQ6IGNhbGMoMTAwdmggLSA4MHB4KTsKICAgICAgICBtYXJnaW4tdG9wOiAyMHB4OwogICAgICAgIG92ZXJmbG93OiBzY3JvbGw7CiAgICAgICAgb3V0bGluZTogMXB4IHNvbGlkIGdyYXk7CiAgICAgIH0KICAgIDwvc3R5bGU+CiAgICA8c2NyaXB0PgogICAgICBmdW5jdGlvbiB1dGY4X3RvX2I2NChzdHIpIHsKICAgICAgICByZXR1cm4gd2luZG93LmJ0b2EodW5lc2NhcGUoZW5jb2RlVVJJQ29tcG9uZW50KHN0cikpKTsKICAgICAgfQogICAgICAvLyBmdW5jdGlvbiBiNjRfdG9fdXRmOChzdHIpIHsKICAgICAgLy8gICByZXR1cm4gZGVjb2RlVVJJQ29tcG9uZW50KGVzY2FwZSh3aW5kb3cuYXRvYihzdHIpKSk7CiAgICAgIC8vIH0KICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoImJ0biIpLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgKCkgPT4gewogICAgICAgIGNvbnN0IGlwdCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoImlucHV0Iik7CiAgICAgICAgY29uc3QgdHh0ID0gYGRhdGE6dGV4dC9odG1sO2Jhc2U2NCwke3V0ZjhfdG9fYjY0KGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoImh0bWwiKS5vdXRlckhUTUwpfWA7CiAgICAgICAgaXB0LnNldEF0dHJpYnV0ZSgidmFsdWUiLCB0eHQpOwogICAgICAgIGRvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoaXB0KTsKICAgICAgICBpcHQuc2V0U2VsZWN0aW9uUmFuZ2UoMCwgdHh0Lmxlbmd0aCk7CiAgICAgICAgaXB0LnNlbGVjdCgpOwogICAgICAgIGRvY3VtZW50LmV4ZWNDb21tYW5kKCJjb3B5Iik7CiAgICAgICAgZG9jdW1lbnQuYm9keS5yZW1vdmVDaGlsZChpcHQpOwogICAgICB9KTsKICAgIDwvc2NyaXB0PgogIAoKPC9ib2R5PjwvaHRtbD4=
		
    20
meeop   
OP
   140 天前
可以的话分享到 urlapp.org 吧,这样别人就能使用这个功能了
参考:
https://urlapp.org/apps/doc2024072200003/howToPublish
发个帖就行
		
    21
stardustree      140 天前
可惜不能直接作为浏览器的默认新标签页，好像是 chrome 有啥限制。否则拿这个自定义一个自己的新标签页还挺方便的。
		
    22
itskingname      140 天前
这个 Data URL 里面并没有包含全部的代码。只有入口 HTML 而已。html 里面可以使用 script 标签导入其他外部的 js 文件和资源。
		
    23
meeop   
OP
   140 天前
@stardustree 你是指启动浏览器的默认页面吗?我试了试可以启动啊,操作路径 [设置]-[启动时]-[打开特定网页或一组网页],然后填 dataurl 或者某个 urlappp 的 html 文件路径都行
		
    24
meeop   
OP
   140 天前
@itskingname Data URL 只是一个编码协议,编码 html 代码到 url.
这个 html 代码可以包含 html+css+js+图片+二进制数据等一切东西

当然,现实中会在 html 中引入各种 web 资源,这种 urlapp 确实不是纯粹的单 html 应用
		
    25
7gugu      140 天前
好好玩
		
    26
superkkk      140 天前    1
玩了一下午你的纸牌游戏都没有通关，最后在网上找了一个百分百有解的玩了一局才通关
		
    27
meeop   
OP
   140 天前
@superkkk 😂😂😂抱歉这个纸牌的实现过于简单了，估计是纯随机不一定有解
		
    28
meeop   
OP
   140 天前
@superkkk 改了下参数,变成超简单版,体验下

data:text/html;base64,CjwhZG9jdHlwZSBodG1sPgo8aHRtbD4KIAogIDxoZWFkPgogICAgPHRpdGxlPkpTMWsgMjAxNiAtIERlbW8gMjYxMiAtICIzIENhcmQgS2xvbmRpa2UiPC90aXRsZT4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KIAogICAgPHNjcmlwdD4KICAgICAgc2V0VGltZW91dChmdW5jdGlvbigpewogICAgICAgIHZhciBnYSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NjcmlwdCcpOwogICAgICAgIGdhLmFzeW5jID0gdHJ1ZTsKICAgICAgICBnYS5kZWZlciA9IHRydWU7CiAgICAgICAgZ2Euc3JjID0gJ2h0dHBzOi8vd3d3Lmdvb2dsZS1hbmFseXRpY3MuY29tL2dhLmpzJzsKICAgICAgICBnYS5vbmxvYWQgPSBmdW5jdGlvbigpe3RyeXtfZ2F0Ll9nZXRUcmFja2VyKCdVQS0xOTg4MjM1My0xJykuX3RyYWNrUGFnZXZpZXcoKTt9Y2F0Y2goZSl7d2luZG93LmNvbnNvbGUmJmNvbnNvbGUubG9nKCJnYSBmYWlsIDonKCAiKTt9O307CiAgICAgICAgdmFyIHMgPSBkb2N1bWVudC5nZXRFbGVtZW50c0J5VGFnTmFtZSgnc2NyaXB0JylbMF07CiAgICAgICAgcy5wYXJlbnROb2RlLmluc2VydEJlZm9yZShnYSwgcyk7CiAgICAgIH0sIDEwKTsKICAgIDwvc2NyaXB0PgogICAgPHN0eWxlPgogICAgICAvKiBodHRwczovL3Fmb3gubmwvbm90ZXMvMzMzICovCiAgICAgIGJvZHksaHRtbCxpZnJhbWV7bWFyZ2luOjA7cGFkZGluZzowO2JvcmRlcjowO3dpZHRoOjEwMCU7aGVpZ2h0OjEwMCV9aWZyYW1le3Bvc2l0aW9uOmFic29sdXRlO3RvcDowO2xlZnQ6MDsKICAgICAgcGFkZGluZy10b3A6NTBweDtib3gtc2l6aW5nOmJvcmRlci1ib3h9IGhlYWRlcntwb3NpdGlvbjpyZWxhdGl2ZTt6LWluZGV4OjE7aGVpZ2h0OjQ3cHg7cGFkZGluZy10b3A6MnB4OwogICAgICBib3JkZXItYm90dG9tOjFweCBzb2xpZCAjMDAwO2JveC1zaGFkb3c6MCAtMTBweCAyNXB4ICNjY2MgaW5zZXQ7YmFja2dyb3VuZC1jb2xvcjojZWVlfSBhc2lkZSxkaXYsaDEscHtvdmVyZmxvdzoKICAgICAgaGlkZGVuO3doaXRlLXNwYWNlOm5vd3JhcDt0ZXh0LW92ZXJmbG93OmVsbGlwc2lzO3RleHQtYWxpZ246Y2VudGVyO2ZvbnQtc2l6ZToxNnB4O2ZvbnQtd2VpZ2h0OmluaGVyaXQ7bGluZS1oZWlnaHQ6CiAgICAgIDIycHg7cGFkZGluZzowO21hcmdpbjowO2N1cnNvcjpkZWZhdWx0fSBhc2lkZSxoMXtkaXNwbGF5OmlubGluZX0gYXtjb2xvcjojMDAwO3RleHQtZGVjb3JhdGlvbjpub25lO2JvcmRlci1ib3R0b206CiAgICAgIDFweCBkYXNoZWQgIzAwMH0gYTpob3Zlcntib3JkZXItYm90dG9tOjFweCBzb2xpZCByZWR9IGFbaHJlZj0iMCJde3RleHQtZGVjb3JhdGlvbjpsaW5lLXRocm91Z2g7cG9pbnRlci1ldmVudHM6bm9uZQogICAgICA7Ym9yZGVyLWJvdHRvbTowO2NvbG9yOiNjY2N9IC5idXR0b257ZmxvYXQ6bGVmdDt3aWR0aDo0MHB4O2hlaWdodDo0MHB4O2xpbmUtaGVpZ2h0OjQwcHg7dGV4dC1hbGlnbjpjZW50ZXI7cGFkZGluZzoKICAgICAgMDttYXJnaW46MnB4IDAgMCAxMHB4O2JvcmRlcjoxcHggc29saWQgIzg4ODtib3JkZXItY29sb3I6I2RkZCAjODg4ICM4ODggI2RkZDtmb250LWZhbWlseTpzYW5zLXNlcmlmO2ZvbnQtc2l6ZTozMHB4CiAgICAgIDtmb250LXdlaWdodDo3MDA7Y3Vyc29yOnBvaW50ZXJ9IC5idXR0b246aG92ZXJ7Y29sb3I6cmVkO2JvcmRlci1ib3R0b20tY29sb3I6Izg4OH0gLnJ7bWFyZ2luLXJpZ2h0OjEwcHh9CiAgICA8L3N0eWxlPgogIDwvaGVhZD4KICA8Ym9keT4KICAgIDxoZWFkZXI+CiAgICAgIDxkaXY+CiAgICAgCiAgICAgICAgPHA+CiAgICAgICAgCiAgICAgICAg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TE9BRF9PTk9SSUVOVEFUSU9OQ0hBTkdFPXRydWUsCiAgICAgIGc9ZG9jdW1lbnQsdD1nLmdldEVsZW1lbnRzQnlUYWdOYW1lKCJoZWFkZXIiKVswXSxrPWcuY3JlYXRlRWxlbWVudCgiaWZyYW1lIik7Zy5ib2R5LmFwcGVuZENoaWxkKGspO3ZhciBhPWsuY29udGVudFdpbmRvdwogICAgICAsYz1rLmNvbnRlbnREb2N1bWVudDtjLm9wZW4oKTtjLmNsb3NlKCk7Yy53cml0ZSgnPCFkb2N0eXBlIGh0bWw+PGh0bWwgc3R5bGU9Im1hcmdpbjogMDsgcGFkZGluZzogMDsgYm9yZGVyOiAwOycrKEI/IiB3IisKICAgICAgImlkdGg6IDEwMCU7IGhlaWdodDogMTAwJTsiOiIiKSsnIj48aGVhZD48bWV0YSBjaGFyc2V0PSJ1dGYtOCI+PGJvZHkgc3R5bGU9Im1hcmdpbjogMDsgcGFkZGluZzogMDsgYm9yZGVyOiAwOycrKEI/IiB3aSIrCiAgICAgICJkdGg6IDEwMCU7IGhlaWdodDogMTAwJTsiOiIiKSsnIj4nKyhCPyc8Y2FudmFzIHN0eWxlPSJkaXNwbGF5OiBibG9jazsnKyhRPyIgbWFyZ2luOiBhdXRvOyI6IiIpKyciPjwvY2FudmFzPic6IiIpKyIiKTtpZgogICAgICAoQil7dmFyIGU9Yy5nZXRFbGVtZW50c0J5VGFnTmFtZSgiY2FudmFzIilbMF0scT1lLnN0eWxlO2MuYm9keS5jbGllbnRXaWR0aDt2YXIgbD1NYXRoLm1heChNYXRoLm1pbihGfHxpbm5lcldpZHRoLAogICAgICBpbm5lcldpZHRoKSwxKSxyPU1hdGgubWF4KE1hdGgubWluKFB8fGlubmVySGVpZ2h0LTUwLGlubmVySGVpZ2h0LTUwKSwxKTsobDxGfHxyPFApJiZVJiYobDxGP3I9bC9GKlA6bD1yL1AqRik7cS53aWR0aD0oZS4KICAgICAgd2lkdGg9bCkrInB4IjtxLmhlaWdodD0oZS5oZWlnaHQ9cikrInB4In1WJiYob25vcmllbnRhdGlvbmNoYW5nZT1oKTthLkF1ZGlvQ29udGV4dD1hLkF1ZGlvQ29udGV4dHx8YS53ZWJraXRBdWRpb0NvbnRleHQ7CiAgICAgIGEucmVxdWVzdEFuaW1hdGlvbkZyYW1lPWEucmVxdWVzdEFuaW1hdGlvbkZyYW1lfHxhLm1velJlcXVlc3RBbmltYXRpb25GcmFtZXx8YS53ZWJraXRSZXF1ZXN0QW5pbWF0aW9uRnJhbWV8fGEuCiAgICAgIG1zUmVxdWVzdEFuaW1hdGlvbkZyYW1lfHxmdW5jdGlvbihiKXthLnNldFRpbWVvdXQoYiwxRTMvMzApfTtCJiYoZS5yZXF1ZXN0UG9pbnRlckxvY2s9ZS5yZXF1ZXN0UG9pbnRlckxvY2t8fGUuCiAgICAgIG1velJlcXVlc3RQb2ludGVyTG9ja3x8ZS53ZWJraXRSZXF1ZXN0UG9pbnRlckxvY2spO2MuYm9keS5yZXF1ZXN0UG9pbnRlckxvY2s9Yy5ib2R5LnJlcXVlc3RQb2ludGVyTG9ja3x8Yy5ib2R5LgogICAgICBtb3pSZXF1ZXN0UG9pbnRlckxvY2t8fGMuYm9keS53ZWJraXRSZXF1ZXN0UG9pbnRlckxvY2s7dmFyIG5hdj1hLm5hdmlnYXRvcjtuYXYuZ2V0VXNlck1lZGlhPW5hdi5nZXRVc2VyTWVkaWF8fE4uCiAgICAgIHdlYmtpdEdldFVzZXJNZWRpYXx8bmF2Lm1vekdldFVzZXJNZWRpYXx8bmF2Lm1zR2V0VXNlck1lZGlhO2EuT3NjaWxsYXRvck5vZGUmJmEuT3NjaWxsYXRvck5vZGUucHJvdG90eXBlJiYoYQogICAgICAuT3NjaWxsYXRvck5vZGUucHJvdG90eXBlLnN0YXJ0PWEuT3NjaWxsYXRvck5vZGUucHJvdG90eXBlLnN0YXJ0fHxhLk9zY2lsbGF0b3JOb2RlLnByb3RvdHlwZS5ub3RlT24sYS5Pc2NpbGxhdG9yTm9kZS4KICAgICAgcHJvdG90eXBlLnN0b3A9YS5Pc2NpbGxhdG9yTm9kZS5wcm90b3R5cGUuc3RvcHx8YS5Pc2NpbGxhdG9yTm9kZS5wcm90b3R5cGUubm90ZU9mZik7QiYmKGEuYT1lKTthLmI9Yy5ib2R5O2EuZD1jO0ImJihOfHwoCiAgICAgIGEuYz1lLmdldENvbnRleHQoIjJkIikpLE4mJihhLmc9ZnVuY3Rpb24oKXthLm9ub3JpZW50YXRpb25jaGFuZ2U9YS5vbnJlc2l6ZT1udWxsO3RyeXt2YXIgYj17YW50aWFsaWFzOiEwLHN0ZW5jaWw6ITB9LGQ9ZQogICAgICAuZ2V0Q29udGV4dCgid2ViZ2wiLGIpfHxlLmdldENvbnRleHQoImV4cGVyaW1lbnRhbC13ZWJnbCIsYik7YS5fX2dsRXh0cz0iT0VTX3RleHR1cmVfZmxvYXQgT0VTX3RleHR1cmVfZmxvYXRfbGluZWFyIE9FIisKICAgICAgIlNfc3RhbmRhcmRfZGVyaXZhdGl2ZXMgRVhUX3RleHR1cmVfZmlsdGVyX2FuaXNvdHJvcGljIE1PWl9FWFRfdGV4dHVyZV9maWx0ZXJfYW5pc290cm9waWMgV0VCS0lUX0VYVF90ZXh0dXJlX2ZpbHRlcl9hbiIrCiAgICAgICJpc290cm9waWMgV0VCR0xfY29tcHJlc3NlZF90ZXh0dXJlX3MzdGMgTU9aX1dFQkdMX2NvbXByZXNzZWRfdGV4dHVyZV9zM3RjIFdFQktJVF9XRUJHTF9jb21wcmVzc2VkX3RleHR1cmVfczN0YyIuc3BsaXQoCiAgICAgICIgIikubWFwKGZ1bmN0aW9uKGEpe3JldHVybiBkLmdldEV4dGVuc2lvbihhKX0pfWNhdGNoKGYpe3Rocm93IGMuYm9keS5pbm5lckhUTUw9IldlYkdMIG5vdCBzdXBwb3J0ZWQuIixhLmE9YS5iPWEuYz1hLmQ9CiAgICAgIG51bGwsZjt9cmV0dXJuIGR9KCkpKTtCPWMuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7Qi50ZXh0Q29udGVudD1nLnF1ZXJ5U2VsZWN0b3IoJ3NjcmlwdFt0eXBlPSJkZW1vIl0nKS50ZXh0Q29udGVudDtjLgogICAgICBib2R5LmFwcGVuZENoaWxkKEIpO2MuY2xvc2UoKTtrLmNvbnRlbnRXaW5kb3cuZm9jdXMoKTtCPWcuZ2V0RWxlbWVudHNCeVRhZ05hbWUoImRpdiIpWzBdO3dpbmRvdy5yZWxvYWQ9aDt2YXIgZD1nLgogICAgICBjcmVhdGVFbGVtZW50KCJkaXYiKTtkLmlubmVySFRNTD0iJiM4NjM1OyI7ZC5jbGFzc05hbWU9ImJ1dHRvbiByIjtkLnRpdGxlPSJyZXN0YXJ0IGp1c3QgdGhlIGRlbW8gKGxvY2FsLCB3aXRob3V0IHJlbW90IisKICAgICAgImUgZmV0Y2gpIjtkLm9uY2xpY2s9aDt0Lmluc2VydEJlZm9yZShkLEIpfSkoKTsKICAgIDwvc2NyaXB0PgogIDwvYm9keT4KPC9odG1sPgo=
		
    29
janus77      140 天前
既然都是从收藏夹点开，那和现在我们用的网页有啥区别
		
    30
Contextualist      140 天前
跳过域名和服务器，没有中间商赚差价（ x
想了想觉得还挺复古的，互联网最初的样子不就是单个 html 文件么
		
    31
meeop   
OP
   140 天前
@janus77
1 保存后网页不会因删除下线而不可用
2 源码形式分发，你可以审查和修改代码
3 代码在本地，无网络延时，加载只要 3ms
4 无广告（或者你改源码删了广告）
5urlapp.org 提供一个分发讨论更新评价的平台
6 对于开发者，发布成本低，免除服务部署，资质认证成本
7 对于分发，你可以直接在文本聊天窗口分发给别人，否则得上传个网盘什么的
		
    32
Takashi123      140 天前
@body007 #19 代码分享为什么着色老是会失效？
		
    33
stardustree      140 天前
@meeop 新标签页，不是“启动时”。浏览器默认不支持自定义，试了几个能自定义 url 的插件，也不支持 data:text/html;
		
    34
body007      140 天前
@Takashi123 我是从 goland 复制然后粘贴到这个编辑框，这个是带格式的。复制的软件要支持复制带格式的数据（否则只能复制纯文本），粘贴时也要那个软件支持相关格式（否则只能粘贴纯文本）。忘记在哪里看到说这个原理的了。
		
    35
meeop   
OP
   140 天前
@stardustree 浏览器出于安全原因,不支持 dataurl 跳转,打开新页面,所以基于浏览器的插件也没法打开一个 dataurl 页面
dataurl 网页只能手动填写到地址栏,或者通过书签等快捷方式打开
但是,你可以把 dataurl 转换为 html 文件,保存到本地,或者发布线上,或者发布到 urlapp.org,然后就有可访问的普通 url 了
		
    36
stardustree      139 天前
@meeop 保存在本地或者发布到线上，跟普通的 url 就没啥优势了。个人理解，这个东西唯一的优势就是轻量。
		
    37
superkkk      139 天前
@meeop 简单是简单了，但是没有办法生成必定有解的游戏
		
    38
meeop   
OP
   139 天前
@stardustree 写了一个工具网页看看能不能用
保存这个网页到本地,网页功能是根据入参的 dataurl 渲染到 iframe,实现普通 url 打开 dataurl

data:text/html;base64,PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9InpoLUNOIj4KCjxoZWFkPgogICAgPG1ldGEgY2hhcnNldD0iVVRGLTgiPgogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiPgogICAgPHRpdGxlPklmcmFtZSDmuLLmn5Plt6Xlhbc8L3RpdGxlPgogICAgPHN0eWxlPgogICAgICAgIGJvZHksCiAgICAgICAgaHRtbCB7CiAgICAgICAgICAgIG1hcmdpbjogMDsKICAgICAgICAgICAgcGFkZGluZzogMDsKICAgICAgICAgICAgd2lkdGg6IDEwMCU7CiAgICAgICAgICAgIGhlaWdodDogMTAwJTsKICAgICAgICB9CgogICAgICAgIGlmcmFtZSB7CiAgICAgICAgICAgIHdpZHRoOiAxMDAlOwogICAgICAgICAgICBoZWlnaHQ6IDEwMCU7CiAgICAgICAgICAgIGJvcmRlcjogbm9uZTsKICAgICAgICB9CiAgICA8L3N0eWxlPgo8L2hlYWQ+Cgo8Ym9keT4KICAgIDxpZnJhbWUgaWQ9ImlmcmFtZSIgc3JjPSIiPjwvaWZyYW1lPgoKICAgIDxzY3JpcHQ+CgogICAgICAgIGZ1bmN0aW9uIGdldFVSTFBhcmFtZXRlcihuYW1lKSB7CiAgICAgICAgICAgIGNvbnN0IHVybFBhcmFtcyA9IG5ldyBVUkxTZWFyY2hQYXJhbXMod2luZG93LmxvY2F0aW9uLnNlYXJjaCk7CiAgICAgICAgICAgIHJldHVybiB1cmxQYXJhbXMuZ2V0KG5hbWUpOwogICAgICAgIH0KCiAgICAgICAgZnVuY3Rpb24gcHJvbXB0Rm9yVVJMKCkgewogICAgICAgICAgICBjb25zdCB1c2VyVVJMID0gcHJvbXB0KCLor7fovpPlhaXopoHliqDovb3nmoRkYXRhdXJs77yaXG7ovpPlhaXnmoR1cmzmlbDmja7kvJrooqvkv53lrZjlnKjmtY/op4jlmajlnLDlnYDmoI8s57G75Ly8eHguaHRtbD91cmw9ZGF0YTp4eHggLOeEtuWQjizkv53lrZjmi7zmjqXlpb3nmoTpk77mjqXljbPlj6/kvZzkuLrmma7pgJp1cmzkvb/nlKgiKTsKICAgICAgICAgICAgaWYgKHVzZXJVUkwpIHsKICAgICAgICAgICAgICAgIGNvbnN0IG5ld1VybCA9IG5ldyBVUkwod2luZG93LmxvY2F0aW9uLmhyZWYpOwogICAgICAgICAgICAgICAgbmV3VXJsLnNlYXJjaFBhcmFtcy5zZXQoJ3VybCcsIHVzZXJVUkwpOwogICAgICAgICAgICAgICAgd2luZG93LmxvY2F0aW9uLmhyZWYgPSBuZXdVcmwudG9TdHJpbmcoKTsKICAgICAgICAgICAgfQogICAgICAgIH0KCiAgICAgICAgKGZ1bmN0aW9uICgpIHsKICAgICAgICAgICAgY29uc3QgdXJsID0gZ2V0VVJMUGFyYW1ldGVyKCd1cmwnKTsKICAgICAgICAgICAgY29uc3QgaWZyYW1lID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lmcmFtZScpOwoKICAgICAgICAgICAgaWYgKHVybCkgewogICAgICAgICAgICAgICAgaWZyYW1lLnNyYyA9IHVybDsKICAgICAgICAgICAgfSBlbHNlIHsKICAgICAgICAgICAgICAgIHByb21wdEZvclVSTCgpOwogICAgICAgICAgICB9CiAgICAgICAgfSkoKTsKICAgIDwvc2NyaXB0Pgo8L2JvZHk+Cgo8L2h0bWw+
		
    39
meeop   
OP
   18 天前
更新进展：


https://genwebapp.com/

升级为支持 ai 编辑的 genwebapp 了，可以直接编辑，发布，并立即可用的 urlapp ，还支持 ai 编辑
关于   ·   帮助文档   ·   博客   ·   API   ·   FAQ   ·   实用小工具   ·   5275 人在线   最高记录 6679   ·      Select Language
创意工作者们的社区
World is powered by solitude
VERSION: 3.9.8.5 · 26ms · UTC 03:31 · PVG 11:31 · LAX 19:31 · JFK 22:31
Developed with CodeLauncher
♥ Do have faith in what you're doing.
