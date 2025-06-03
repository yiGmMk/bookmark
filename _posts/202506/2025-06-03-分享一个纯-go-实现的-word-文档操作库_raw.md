---
layout: post
---
Title: 分享一个纯 Go 实现的 Word 文档操作库 - WordZero - V2EX

URL Source: https://www.v2ex.com/t/1135912

Published Time: 2025-06-03T01:00:05Z

Markdown Content:
最近在做一个项目需要生成 Word 报告，试了几个库都不太满意，要么功能太简单，要么需要付费不完全开源。索性自己撸了一个，现在分享给大家。

为什么又造轮子？
--------

市面上的 Go Word 库要么只能做简单的文本插入，要么需要安装 Office 或者 LibreOffice 。我需要的是：

*   纯 Go 实现，无外部依赖
*   支持复杂的表格操作
*   能处理样式和格式
*   性能要好，适合批量生成

主要特性
----

### 基础功能

*   创建/读取/修改 .docx 文档
*   文本格式化（字体、颜色、粗体等）
*   18 种预定义样式，支持 Word 导航窗格
*   段落对齐、间距、缩进

### 表格功能（这个比较实用）

```
// 创建表格很简单
table := doc.AddTable(&document.TableConfig{
    Rows: 3, Columns: 4,
})

// 设置内容和样式
table.SetCellText(0, 0, "姓名")
table.MergeCells(0, 0, 0, 1) // 合并单元格

// 还有迭代器，方便批量处理
table.ForEach(func(info *document.CellInfo) {
    if info.Row == 0 {
        info.Cell.SetBackgroundColor("E6F3FF")
    }
})
```

### 模板功能

支持模板继承，可以定义基础模板然后扩展：

```
baseTemplate := `{{companyName}} 报告
{{#block "content"}}默认内容{{/block}}`

salesTemplate := `{{extends "base"}}
{{#block "content"}}
销售额：{{sales}}
新客户：{{customers}}
{{/block}}`
```

### 高级功能

*   页眉页脚、目录生成
*   脚注尾注、列表编号
*   页面设置（ A4 、Letter 等）
*   图片插入

性能表现
----

做了个简单的基准测试，生成同样的文档：

*   **Go (WordZero)**: 2.62ms
*   JavaScript: 9.63ms 
*   Python: 55.98ms

Go 确实快不少。

使用体验
----

API 设计比较直观，支持链式调用：

```
doc := document.New()

doc.AddParagraph("标题").
    SetStyle(style.StyleHeading1).
    SetAlignment(document.AlignmentCenter)

doc.AddParagraph("正文内容").
    SetFontFamily("微软雅黑").
    SetFontSize(12).
    SetColor("333333")

doc.Save("report.docx")
```

项目地址
----

GitHub: [https://github.com/ZeroHawkeye/wordZero](https://github.com/ZeroHawkeye/wordZero)

Gitee: [https://gitee.com/Zmata_admin/WordZero](https://gitee.com/Zmata_admin/WordZero)

有详细的文档和示例，examples 目录下有各种使用场景的 demo 。

适用场景
----

*   报表生成系统
*   合同文档批量生成 
*   数据导出为 Word 格式
*   文档模板填充
*   自动化办公

目前还在持续更新中，如果有需求或者 bug 欢迎提 issue 。

* * *

_纯 Go 实现，零依赖，开箱即用。如果对你有帮助记得给个 star ⭐_

![Image 1: wangritian](https://cdn.v2ex.com/avatar/acd6/85e6/497030_normal.png?m=1711472308)1

**[wangritian](https://www.v2ex.com/member/wangritian)**2 小时 23 分钟前
go 确实没有好用的开源 word 操作库，之前是 kotlin 接 apache 那套然后用 cgo 调用 jar 曲线救国的，star 支持一下

![Image 2: jazzychai](https://cdn.v2ex.com/avatar/e71d/b23f/168706_normal.png?m=1516760029)2

**[jazzychai](https://www.v2ex.com/member/jazzychai)**2 小时 9 分钟前
star 了，刚好要做一个 word 相关的功能，本来想用 Python 曲线救国，试一下能不能满足业务需求

![Image 3: moell](https://cdn.v2ex.com/avatar/1205/9742/192194_normal.png?m=1738904748)8

**[moell](https://www.v2ex.com/member/moell)**1 小时 24 分钟前
已 star

![Image 4: 676529483](https://cdn.v2ex.com/avatar/e129/50d6/352970_normal.png?m=1674873037)9

**[676529483](https://www.v2ex.com/member/676529483)**1 小时 18 分钟前![Image 5: ❤️](https://www.v2ex.com/static/img/heart_neue_red.png?v=16ec2dd0a880be6edda1e4a2e35754b3) 1
支持下，以前有个项目要用 xls ，go 只支持 xlsx ，最后只能 Python 曲线救国了

![Image 6: caotian](https://cdn.v2ex.com/gravatar/3714e83484ebd70b56ed11d2df86323a?s=48&d=retro)10

**[caotian](https://www.v2ex.com/member/caotian)**1 小时 17 分钟前
已 start, 有没有图表支持? 如果有的话, 就可以换掉 poi-tl 那套了, 那个库报了 Vulnerability 一直不更新修复, 快不敢用了.

![Image 7: dbskcnc](https://cdn.v2ex.com/avatar/144c/f058/230943_normal.png?m=1659945817)11

**[dbskcnc](https://www.v2ex.com/member/dbskcnc)**1 小时 10 分钟前
虽然基本不用 word,不过还是支持

![Image 8: vfs](https://cdn.v2ex.com/avatar/ec20/25a5/583944_normal.png?m=1728985857)13

**[vfs](https://www.v2ex.com/member/vfs)**34 分钟前
目前还没有需求，但是很赞

![Image 9: lexno](https://cdn.v2ex.com/gravatar/7a4abac3f161e701fde7f416d420e6fd?s=48&d=retro)17

**[lexno](https://www.v2ex.com/member/lexno)**几秒前
支不支持已有的 word 模板，然后使用这个模板来生成数据，我看现有的示例好像都是用库本身产生一个 document ，然后再进行模板填充？

