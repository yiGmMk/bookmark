---
layout: post
---
Title: 利用GitHub Actions自动对仓库内图片进行无损压缩

URL Source: https://wiki.eryajf.net/pages/dbee9e/

Published Time: 2022-08-01T23:42:32.000Z

Markdown Content:
利用GitHub Actions自动对仓库内图片进行无损压缩 | 二丫讲梵

===============

[![Image 3: 二丫讲梵](https://wiki.eryajf.net/img/logo.png)二丫讲梵](https://wiki.eryajf.net/)

[首页](https://wiki.eryajf.net/)

[运维](https://wiki.eryajf.net/ops/)运维
*   [最佳实践](https://wiki.eryajf.net/best-practices/)
*   [迎刃而解](https://wiki.eryajf.net/solve-it/)
*   [Nginx](https://wiki.eryajf.net/nginx/)
*   [Php](https://wiki.eryajf.net/php/)
*   [Zabbix](https://wiki.eryajf.net/zabbix/)
*   [AWS](https://wiki.eryajf.net/aws/)
*   [Prometheus](https://wiki.eryajf.net/prometheus/)
*   [Grafana](https://wiki.eryajf.net/grafana/)
*   [CentOS](https://wiki.eryajf.net/centos/)
*   [Systemd](https://wiki.eryajf.net/systemd/)
*   [Docker](https://wiki.eryajf.net/docker/)
*   [Rancher](https://wiki.eryajf.net/rancher/)
*   [Ansible](https://wiki.eryajf.net/ansible/)
*   [Ldap](https://wiki.eryajf.net/OpenLdap/)
*   [Gitlab](https://wiki.eryajf.net/gitlab/)
*   [GitHub](https://wiki.eryajf.net/github/)
*   [Etcd](https://wiki.eryajf.net/etcd/)
*   [Consul](https://wiki.eryajf.net/consul/)
*   [RabbitMQ](https://wiki.eryajf.net/RabbitMQ/)
*   [Kafka](https://wiki.eryajf.net/kafka/)
*   [MySql](https://wiki.eryajf.net/mysql/)
*   [MongoDB](https://wiki.eryajf.net/MongoDB/)
*   [OpenVPN](https://wiki.eryajf.net/OpenVPN/)
*   [KVM](https://wiki.eryajf.net/kvm/)
*   [VMware](https://wiki.eryajf.net/VMware/)
*   [Other](https://wiki.eryajf.net/other/)

[专题](https://wiki.eryajf.net/topic/)专题
*   [ELK](https://wiki.eryajf.net/elk/)
*   [K8S](https://wiki.eryajf.net/k8s/)
*   [LLM](https://wiki.eryajf.net/llm/)
*   [Nexus](https://wiki.eryajf.net/nexus/)
*   [Jenkins](https://wiki.eryajf.net/jenkins/)

[生活](https://wiki.eryajf.net/life/)生活
*   [随写编年](https://wiki.eryajf.net/sxbn/)
*   [家人物语](https://wiki.eryajf.net/jrwy/)
*   [追忆青春](https://wiki.eryajf.net/zyqc/)
*   [父亲的朋友圈](https://wiki.eryajf.net/fqdpyq/)
*   [电影音乐](https://wiki.eryajf.net/dyyy/)
*   [效率工具](https://wiki.eryajf.net/xlgj/)
*   [博客相关](https://wiki.eryajf.net/bkxg/)

[编程](https://wiki.eryajf.net/code/)编程
*   [Shell](https://wiki.eryajf.net/shell/)
*   [前端实践](https://wiki.eryajf.net/front-code/)
*   [Vue学习笔记](https://wiki.eryajf.net/vue-learn/)
*   [Golang学习笔记](https://wiki.eryajf.net/go-learn/)
*   [Golang编程技巧](https://wiki.eryajf.net/go-code/)

[周刊](https://wiki.eryajf.net/weekly/)周刊
*   [学习周刊](https://wiki.eryajf.net/learning-weekly/)
*   [Obsidian插件周刊](https://wiki.eryajf.net/obsidian-weekly/)

[关于](https://wiki.eryajf.net/about/)

[友链](https://wiki.eryajf.net/friends/)

[页面](https://wiki.eryajf.net/nav/)页面
*   #### 本站索引

    *   [分类](https://wiki.eryajf.net/categories/)
    *   [标签](https://wiki.eryajf.net/tags/)
    *   [归档](https://wiki.eryajf.net/archives/)

*   #### 本站页面

    *   [导航](https://wiki.eryajf.net/nav/)
    *   [打赏](https://wiki.eryajf.net/reward/)

*   #### 我的工具

    *   [备忘录清单 (opens new window)](https://ref.eryajf.net/)
    *   [json2go (opens new window)](http://public.eryajf.net/json2go)
    *   [gopher (opens new window)](http://gopher.eryajf.net/)
    *   [微信MD编辑 (opens new window)](http://public.eryajf.net/mdnice)
    *   [国内镜像 (opens new window)](http://public.eryajf.net/mirror)
    *   [出口IP查询 (opens new window)](http://ip.eryajf.net/)
    *   [代码高亮工具 (opens new window)](http://public.eryajf.net/highlight/)

*   #### 外站页面

    *   [开往 (opens new window)](https://www.travellings.cn/go.html)
    *   [ldapdoc (opens new window)](http://ldapdoc.eryajf.net/)
    *   [HowToStartOpenSource (opens new window)](https://howtosos.eryajf.net/)
    *   [vdoing-template (opens new window)](https://eryajf.github.io/vdoing-template/)

[GitHub (opens new window)](https://github.com/eryajf)

![Image 4](https://y.gtimg.cn/music/photo_new/T053M000003qCkuI3Qswd4.jpg)

### 二丫讲梵

行者常至，为者常成

[首页](https://wiki.eryajf.net/)

[运维](https://wiki.eryajf.net/ops/)运维
*   [最佳实践](https://wiki.eryajf.net/best-practices/)
*   [迎刃而解](https://wiki.eryajf.net/solve-it/)
*   [Nginx](https://wiki.eryajf.net/nginx/)
*   [Php](https://wiki.eryajf.net/php/)
*   [Zabbix](https://wiki.eryajf.net/zabbix/)
*   [AWS](https://wiki.eryajf.net/aws/)
*   [Prometheus](https://wiki.eryajf.net/prometheus/)
*   [Grafana](https://wiki.eryajf.net/grafana/)
*   [CentOS](https://wiki.eryajf.net/centos/)
*   [Systemd](https://wiki.eryajf.net/systemd/)
*   [Docker](https://wiki.eryajf.net/docker/)
*   [Rancher](https://wiki.eryajf.net/rancher/)
*   [Ansible](https://wiki.eryajf.net/ansible/)
*   [Ldap](https://wiki.eryajf.net/OpenLdap/)
*   [Gitlab](https://wiki.eryajf.net/gitlab/)
*   [GitHub](https://wiki.eryajf.net/github/)
*   [Etcd](https://wiki.eryajf.net/etcd/)
*   [Consul](https://wiki.eryajf.net/consul/)
*   [RabbitMQ](https://wiki.eryajf.net/RabbitMQ/)
*   [Kafka](https://wiki.eryajf.net/kafka/)
*   [MySql](https://wiki.eryajf.net/mysql/)
*   [MongoDB](https://wiki.eryajf.net/MongoDB/)
*   [OpenVPN](https://wiki.eryajf.net/OpenVPN/)
*   [KVM](https://wiki.eryajf.net/kvm/)
*   [VMware](https://wiki.eryajf.net/VMware/)
*   [Other](https://wiki.eryajf.net/other/)

[专题](https://wiki.eryajf.net/topic/)专题
*   [ELK](https://wiki.eryajf.net/elk/)
*   [K8S](https://wiki.eryajf.net/k8s/)
*   [LLM](https://wiki.eryajf.net/llm/)
*   [Nexus](https://wiki.eryajf.net/nexus/)
*   [Jenkins](https://wiki.eryajf.net/jenkins/)

[生活](https://wiki.eryajf.net/life/)生活
*   [随写编年](https://wiki.eryajf.net/sxbn/)
*   [家人物语](https://wiki.eryajf.net/jrwy/)
*   [追忆青春](https://wiki.eryajf.net/zyqc/)
*   [父亲的朋友圈](https://wiki.eryajf.net/fqdpyq/)
*   [电影音乐](https://wiki.eryajf.net/dyyy/)
*   [效率工具](https://wiki.eryajf.net/xlgj/)
*   [博客相关](https://wiki.eryajf.net/bkxg/)

[编程](https://wiki.eryajf.net/code/)编程
*   [Shell](https://wiki.eryajf.net/shell/)
*   [前端实践](https://wiki.eryajf.net/front-code/)
*   [Vue学习笔记](https://wiki.eryajf.net/vue-learn/)
*   [Golang学习笔记](https://wiki.eryajf.net/go-learn/)
*   [Golang编程技巧](https://wiki.eryajf.net/go-code/)

[周刊](https://wiki.eryajf.net/weekly/)周刊
*   [学习周刊](https://wiki.eryajf.net/learning-weekly/)
*   [Obsidian插件周刊](https://wiki.eryajf.net/obsidian-weekly/)

[关于](https://wiki.eryajf.net/about/)

[友链](https://wiki.eryajf.net/friends/)

[页面](https://wiki.eryajf.net/nav/)页面
*   #### 本站索引

    *   [分类](https://wiki.eryajf.net/categories/)
    *   [标签](https://wiki.eryajf.net/tags/)
    *   [归档](https://wiki.eryajf.net/archives/)

*   #### 本站页面

    *   [导航](https://wiki.eryajf.net/nav/)
    *   [打赏](https://wiki.eryajf.net/reward/)

*   #### 我的工具

    *   [备忘录清单 (opens new window)](https://ref.eryajf.net/)
    *   [json2go (opens new window)](http://public.eryajf.net/json2go)
    *   [gopher (opens new window)](http://gopher.eryajf.net/)
    *   [微信MD编辑 (opens new window)](http://public.eryajf.net/mdnice)
    *   [国内镜像 (opens new window)](http://public.eryajf.net/mirror)
    *   [出口IP查询 (opens new window)](http://ip.eryajf.net/)
    *   [代码高亮工具 (opens new window)](http://public.eryajf.net/highlight/)

*   #### 外站页面

    *   [开往 (opens new window)](https://www.travellings.cn/go.html)
    *   [ldapdoc (opens new window)](http://ldapdoc.eryajf.net/)
    *   [HowToStartOpenSource (opens new window)](https://howtosos.eryajf.net/)
    *   [vdoing-template (opens new window)](https://eryajf.github.io/vdoing-template/)

[GitHub (opens new window)](https://github.com/eryajf)
*   最佳实践

*   迎刃而解

*   Nginx

*   Php

*   Zabbix

*   AWS

*   Prometheus

*   Grafana

*   Loki

*   CentOS

*   Supervisord

*   Systemd

*   Docker

*   Docker-Compose

*   Rancher

*   Ansible

*   OpenLdap

*   GitLab

*   GitHub

    *   [GitHub中开源项目维护流程手册](https://wiki.eryajf.net/pages/53399c/)
    *   [分享我的开源项目Thank-Mirror](https://wiki.eryajf.net/pages/e7a8dc/)
    *   [2024年重磅开源项目 awesome-ops 已收录项目500个](https://wiki.eryajf.net/pages/9dfb86/)
    *   [分享我的开源项目Cloud_Dns_Exporter，妈妈再也不担心我忘换证书了](https://wiki.eryajf.net/pages/a47486/)
    *   [一个仅需三步配置就能生成免费个人博客的开源模板vdoing-template](https://wiki.eryajf.net/pages/48e307/)
    *   [如何将个人的GitHub主页配置的优雅好看](https://wiki.eryajf.net/pages/d195b4/)
    *   [利用GitHub Actions自动为README添加TOC目录](https://wiki.eryajf.net/pages/226388/)
    *   [利用GitHub Actions自动将项目贡献者列表添加到README中](https://wiki.eryajf.net/pages/2cb154/)
    *   [利用GitHub Actions自动优雅地为项目构建Releases](https://wiki.eryajf.net/pages/f3e878/)
    *   [利用GitHub Actions自动获取博客rss文章](https://wiki.eryajf.net/pages/1b1ba3/)
    *   [利用GitHub Actions自动构建项目的docker镜像并发布到DockerHub](https://wiki.eryajf.net/pages/5baf0a/)
    *   [利用GitHub Actions自动生成GitHub的Fans](https://wiki.eryajf.net/pages/db92f0/)
    *   [利用GitHub Actions自动生成个人star列表并归类](https://wiki.eryajf.net/pages/4ba0f4/)
    *   [利用GitHub Actions自动对仓库内图片进行无损压缩](https://wiki.eryajf.net/pages/dbee9e/)
    *   [利用GitHub Actions自动检测项目中的问题链接](https://wiki.eryajf.net/pages/c78b38/)
    *   [利用GitHub Actions自动构建go项目的二进制到release](https://wiki.eryajf.net/pages/d16f3f/)
    *   [利用github-slug-action暴漏Github Action上下文中的关键变量](https://wiki.eryajf.net/pages/77e2fe/)
    *   [利用Github Action自动检测项目中 yaml 或 json 的语法](https://wiki.eryajf.net/pages/dde9ca/)
    *   [记录最近在Github Action配置实践中的几个新的收获](https://wiki.eryajf.net/pages/67c388/)
    *   [VMR一个开源的通用SDK版本管理器](https://wiki.eryajf.net/pages/b75b17/)

*   Etcd

*   Consul

*   RabbitMQ

*   Kafka

*   Mysql

*   MongoDB

*   OpenVPN

*   Kvm

*   VMware

*   配置文件详解

*   Other

*   [](https://wiki.eryajf.net/ "首页")
*   [运维观止](https://wiki.eryajf.net/categories/?category=%E8%BF%90%E7%BB%B4%E8%A7%82%E6%AD%A2 "分类")
*   [GitHub](https://wiki.eryajf.net/categories/?category=GitHub "分类")

[二丫讲梵](https://github.com/eryajf "作者")

[2022-08-01](javascript:;)

![Image 5](blob:http://localhost/2c23c67aae8891567e1e265b5c98d8b1)利用GitHub Actions自动对仓库内图片进行无损压缩
================================================================================================

 文章发布较早，内容可能过时，阅读注意甄别。 

我维护的 [awesome-github-profile-readme-chinese(opens new window)](https://github.com/eryajf/awesome-github-profile-readme-chinese) 项目旨在收集汇总中文区优秀的个人主页，每个人的主页将会通过截图的方式存放在 exampls 目录下，有时候有的朋友主页内容很多，这样整体截图下来就非常大。

本文就介绍一个有意思的小动作，它的主要功能是可以自动扫描仓库内的图片，然后对其进行几乎无损的压缩，让整个仓库的体积保持在一个相对低的水平。

所用 Actions：[image-actions(opens new window)](https://github.com/calibreapp/image-actions)

使用配置其实非常简单，基本上阅读完官方介绍文档就可以上手使用了，这里说一两个需要注意的地方。

首先添加 Actions 配置文件，e.g.`.github/workflows/images.yml`：

```
name: 压缩图片
on:
  push:
    branches:
      - main
    paths:
      - "**.jpg"
      - "**.jpeg"
      - "**.png"
      - "**.webp"
  workflow_dispatch:
jobs:
  build:
    name: calibreapp/image-actions
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v2
      - name: Compress Images
        id: calibre
        uses: calibreapp/image-actions@main
        with:
          githubToken: ${{ secrets.GITHUB_TOKEN }}
          compressOnly: true
          jpegQuality: "60"
          jpegProgressive: false
          pngQuality: "60"
          webpQuality: "60"
      - name: Create New Pull Request If Needed
        if: steps.calibre.outputs.markdown != ''
        uses: peter-evans/create-pull-request@v3
        with:
          title: "🛠 压缩图片"
          branch-suffix: timestamp
          commit-message: "🛠 压缩图片"
          body: ${{ steps.calibre.outputs.markdown }}
```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

需要注意，压缩图片的动作，在运行之后，会自动将图片二次 commit 上来，这就要求该动作具有对应 commit 的权限才行，通常我们配置的 token 没有其他开发者 fork 之后的仓库的权限，于是这里并不能直接处理其他人 PR 过来的内容中的图片。

官方给出的建议是：

*   要么其他开发者通过在主仓库 check 一个分支，然后在主仓库进行分支的 PR。但这种方式其实并非是 GitHub 中协作的主流场景，多用在开发者个人维护的流程。
*   要么就是先处理其他人通过 fork 的方式提交上来的 PR，当 PR 被同意之后，会自动进行扫描检查，然后该动作完成图片压缩之后，再自动创建一个新的 PR，来完成图片的压缩。

还需要注意的一点是：其中的 `secrets.GITHUB_TOKEN`是操作当前仓库使用的，不需要进行更改，如果改了，反而会报错。

效果如下：

![Image 6](https://t.eryajf.net/imgs/2022/08/1fa538021f1f5631.png)

这个动作会自动将图片处理好，然后提交到当次 PR 上，我们可以点开 View diff 查看前后的区别：

![Image 7](https://t.eryajf.net/imgs/2022/08/92fefdc809ad227d.png)

目前这个效果据我个人放大前后两张照片来看，在体积缩小了 80%的情况下，清晰度几乎是一致的，还是非常给力的一个动作，适合那些存放图片比较多的仓库。

打赏

![Image 8: 微信](https://t.eryajf.net/imgs/2023/01/834f12107ebc432a.png)![Image 9: 支付宝](https://t.eryajf.net/imgs/2023/01/fc21022aadd292ca.png)

上次更新:2024/09/26, 21:41:44

[利用GitHub Actions自动生成个人star列表并归类](https://wiki.eryajf.net/pages/4ba0f4/)[利用GitHub Actions自动检测项目中的问题链接](https://wiki.eryajf.net/pages/c78b38/)

← [利用GitHub Actions自动生成个人star列表并归类](https://wiki.eryajf.net/pages/4ba0f4/)[利用GitHub Actions自动检测项目中的问题链接](https://wiki.eryajf.net/pages/c78b38/)→

[最近更新](https://wiki.eryajf.net/archives/)

01[学习周刊-总第213期-2025年第22周](https://wiki.eryajf.net/pages/e0965e/)05-29 02[学习周刊-总第212期-2025年第21周](https://wiki.eryajf.net/pages/ae0d2f/)05-22 03[从赵心童世锦赛夺冠聊聊我的斯诺克情缘](https://wiki.eryajf.net/pages/a49f60/)05-16[更多文章>](https://wiki.eryajf.net/archives/)

[](https://github.com/eryajf "GitHub")[](mailto:eryajf@gmail.com "发邮件")[](https://wiki.eryajf.net/rss.xml "订阅")

 Theme by [Vdoing](https://github.com/xugaoyi/vuepress-theme-vdoing "本站主题") | Copyright © 2017-2025 | [![Image 10: 点击查看十年之约](https://t.eryajf.net/imgs/2022/01/964560013b68c2e4.png) |](https://www.foreverblog.cn/)[浙ICP备18057030号](https://beian.miit.gov.cn/)

*    跟随系统 
*    浅色模式 
*    深色模式 
*    阅读模式

