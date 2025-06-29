---
layout: post
---
Title: Linux 系统 OOM 排查指南_Linux 笔记

URL Source: https://tendcode.com/subject/article/linux-oom/

Published Time: 2025-04-29T10:59:27+00:00

Markdown Content:
Linux 系统 OOM 排查指南_[Linux]学习笔记_编程笔记_TendCode

===============
[**TendCode**](https://tendcode.com/)

*   [首页(current)](https://tendcode.com/)
*   [专题](https://tendcode.com/subject/)
*   [归档](https://tendcode.com/archive/)
*   [在线工具](https://tendcode.com/tool/)
*   [扩展功能](https://tendcode.com/subject/article/linux-oom/#)[网址导航](https://tendcode.com/nav/ "个人的导航网站")[Feed Hub](https://tendcode.com/feed-hub/ "个人的内容聚合平台")[监控Demo](https://tendcode.com/monitor/demo)[运动看板](https://tendcode.com/health/)[端口大全](https://tendcode.com/port/)[流程设计](https://tendcode.com/flow/) 
*   [个人外链](https://tendcode.com/subject/article/linux-oom/#)[Github](https://github.com/Hopetree "我的Github，专注写Bug")[个人文档](https://hopetree.github.io/ "我的个人文档，使用Vitepress搭建") 
*   [友情链接](https://tendcode.com/friend/)
*   [关于](https://tendcode.com/about/)

*   [登录](https://tendcode.com/accounts/login/?next=/subject/article/linux-oom/)
*   [注册](https://tendcode.com/accounts/signup/?next=/subject/article/linux-oom/)

**Linux**

*   安装升级   
    *   [VMware虚拟机桥接网络设置固定静态IP](https://tendcode.com/subject/article/vmware-bridged-network/)
    *   [VirtualBox 安装 CentOS 7 系统并通过主机 ssh 连接虚拟机](https://tendcode.com/subject/article/virtualbox-install-centos7/)

*   学习笔记   
    *   [Linux 系统 OOM 排查指南](https://tendcode.com/subject/article/linux-oom/)
    *   [记录一些在持续部署中可复用的shell命令和函数](https://tendcode.com/subject/article/shell-functions-and-commands/)
    *   [Linux系统中负载过高问题的排查思路与解决方案](https://tendcode.com/subject/article/Linux-Load-Average/)
    *   [检查服务器端口连通性的几种方法](https://tendcode.com/subject/article/port-check/)
    *   [Linux 三剑客（grep awk sed）常用操作笔记](https://tendcode.com/subject/article/grep-awk-sed/)
    *   [Linux 学习笔记 ——第（1）期](https://tendcode.com/subject/article/study-linux-01/)

*   案例分享   
    *   [使用curl命令获取请求接口每个阶段的耗时](https://tendcode.com/subject/article/curl-time/)
    *   [rsync 实时同步方案](https://tendcode.com/subject/article/rsync/)
    *   [Linux 设置 SSH 密钥登陆及更换登录端口](https://tendcode.com/subject/article/ssh-id_rsa/)
    *   [Linux 上使用 crontab 设置定时任务及运行 Python 代码不执行的解决方案](https://tendcode.com/subject/article/hello-crontab/)

*   资源分享   
    *   [分享一些常用的更换各种“源”的经验](https://tendcode.com/subject/article/sources-conf/)

1.   [首页](https://tendcode.com/)
2.   [Linux](https://tendcode.com/subject/4/)
3.    Linux 系统 OOM 排查指南 
4.    当前文章 

Linux 系统 OOM 排查指南
=================

* * *

发表于 2025年04月29日 阅读 599 评论 0

OOM 介绍
------

**OOM（Out of Memory，内存不足）** 是指 Linux 系统中可用内存资源耗尽的情况。当系统中的进程占用的内存总量超过了系统可用的物理内存和交换空间时，就会触发 OOM。这种情况通常发生在以下场景：

*   系统负载过高，大量进程同时运行并占用大量内存。
*   某些进程存在内存泄漏问题，不断消耗内存资源。
*   系统配置的内存资源不足，无法满足当前运行的应用程序需求。

当 OOM 发生时，内核会触发 **OOM Killer** 机制，自动选择并杀掉某些进程以释放内存资源，从而避免系统完全崩溃。然而，被杀掉的进程可能包括关键服务，这会导致服务中断、数据丢失或系统性能严重下降。

一、查看系统日志
--------

### 1.1 dmesg 命令

bash

Copy
```bash
dmesg | grep -i "killed process"
```

或

bash

Copy
```bash
dmesg | grep -i "out of memory"
```

**输出示例：**

text

Copy
```text
[12345.678901] Out of memory: Kill process 1234 (java) score 987 or sacrifice child
[12345.678902] Killed process 1234 (java) total-vm:204800kB, anon-rss:102400kB, file-rss:512kB
```

说明系统确实触发了 OOM，并显示被 kill 的进程信息。

### 1.2 查看日志文件

bash

Copy
```bash
grep -i 'killed process' /var/log/messages
```

或

bash

Copy
```bash
grep -i 'oom' /var/log/syslog
```

**不同系统日志文件：**

*   RHEL/CentOS：`/var/log/messages`
*   Debian/Ubuntu：`/var/log/syslog`

二、使用 journalctl（适用于 systemd 系统）
-------------------------------

bash

Copy
```bash
journalctl -k | grep -i 'killed process'
```

结合时间范围查询最近记录：

bash

Copy
```bash
journalctl -k --since "1 hour ago" | grep -i 'oom'
```

三、排查内存使用情况
----------

### 3.1 查看内存使用历史（搭配监控工具）

如果部署了监控平台（如 Prometheus + Grafana、Zabbix、Nagios），可查看以下指标趋势图：

*   Memory usage 
*   Cache 
*   Swap usage 
*   OOM Kill 指标

重点关注是否有突发性内存飙升。

### 3.2 查看进程内存使用情况（实时 / 手动）

bash

Copy
```bash
top
```

或

bash

Copy
```bash
htop
```

或

bash

Copy
```bash
ps aux --sort=-%mem | head -n 10
```

四、查看 OOM 统计信息
-------------

### 4.1 查看进程 OOM 评分

查看某个进程触发 OOM 的可能性评分（数值越高，被杀概率越大）：

bash

Copy
```bash
cat /proc/<pid>/oom_score
```

五、其他建议
------

*   启用 `vm.panic_on_oom=1` 可在发生 OOM 时触发内核 panic（仅限高可靠系统，慎用）。 
*   启用 cgroups 限制内存使用的容器或服务，避免影响整个系统。 
*   在被 OOM 的服务中设置日志，间接确认异常退出原因。

总结
--

| 方法 | 说明 |
| --- | --- |
| dmesg / journalctl | 快速查看内核日志中是否有 OOM Kill |
| /var/log/messages / syslog | 系统级日志查看历史 OOM 信息 |
| oom_score | 检查进程被 OOM Kill 的风险 |
| 监控系统 | 排查内存异常变化的时段和趋势 |

> **版权声明：**如无特殊说明，文章均为本站原创，转载请注明出处
> 
> 
> **本文链接：**https://tendcode.com/subject/article/linux-oom/
> 
> 
> **许可协议：**[署名-非商业性使用 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc/4.0/)

[Linux](https://tendcode.com/tag/Linux/)[OOM](https://tendcode.com/tag/OOM/)

*   [上一篇](https://tendcode.com/subject/article/virtualbox-install-centos7/)
*   [下一篇](https://tendcode.com/subject/article/shell-functions-and-commands/)

您尚未登录，请 [登录](https://tendcode.com/accounts/login/?next=/subject/article/linux-oom/) 或 [注册](https://tendcode.com/accounts/signup/?next=/subject/article/linux-oom/) 后评论 

[](https://tendcode.com/accounts/weibo/login/?next=/subject/article/linux-oom/ "社交账号登录有点慢，请耐心等候！")[](https://tendcode.com/accounts/github/login/?next=/subject/article/linux-oom/ "社交账号登录有点慢，请耐心等候！")

**0 人参与|0 条评论**

 暂时没有评论，欢迎来尬聊！ 

**大纲**

*   [OOM 介绍](https://tendcode.com/subject/article/linux-oom/#oom-%E4%BB%8B%E7%BB%8D)
*   [一、查看系统日志](https://tendcode.com/subject/article/linux-oom/#%E4%B8%80%E6%9F%A5%E7%9C%8B%E7%B3%BB%E7%BB%9F%E6%97%A5%E5%BF%97)
    *   [1.1 dmesg 命令](https://tendcode.com/subject/article/linux-oom/#11-dmesg-%E5%91%BD%E4%BB%A4)
    *   [1.2 查看日志文件](https://tendcode.com/subject/article/linux-oom/#12-%E6%9F%A5%E7%9C%8B%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6)

*   [二、使用 journalctl（适用于 systemd 系统）](https://tendcode.com/subject/article/linux-oom/#%E4%BA%8C%E4%BD%BF%E7%94%A8-journalctl%E9%80%82%E7%94%A8%E4%BA%8E-systemd-%E7%B3%BB%E7%BB%9F)
*   [三、排查内存使用情况](https://tendcode.com/subject/article/linux-oom/#%E4%B8%89%E6%8E%92%E6%9F%A5%E5%86%85%E5%AD%98%E4%BD%BF%E7%94%A8%E6%83%85%E5%86%B5)
    *   [3.1 查看内存使用历史（搭配监控工具）](https://tendcode.com/subject/article/linux-oom/#31-%E6%9F%A5%E7%9C%8B%E5%86%85%E5%AD%98%E4%BD%BF%E7%94%A8%E5%8E%86%E5%8F%B2%E6%90%AD%E9%85%8D%E7%9B%91%E6%8E%A7%E5%B7%A5%E5%85%B7)
    *   [3.2 查看进程内存使用情况（实时 / 手动）](https://tendcode.com/subject/article/linux-oom/#32-%E6%9F%A5%E7%9C%8B%E8%BF%9B%E7%A8%8B%E5%86%85%E5%AD%98%E4%BD%BF%E7%94%A8%E6%83%85%E5%86%B5%E5%AE%9E%E6%97%B6-%E6%89%8B%E5%8A%A8)

*   [四、查看 OOM 统计信息](https://tendcode.com/subject/article/linux-oom/#%E5%9B%9B%E6%9F%A5%E7%9C%8B-oom-%E7%BB%9F%E8%AE%A1%E4%BF%A1%E6%81%AF)
    *   [4.1 查看进程 OOM 评分](https://tendcode.com/subject/article/linux-oom/#41-%E6%9F%A5%E7%9C%8B%E8%BF%9B%E7%A8%8B-oom-%E8%AF%84%E5%88%86)

*   [五、其他建议](https://tendcode.com/subject/article/linux-oom/#%E4%BA%94%E5%85%B6%E4%BB%96%E5%BB%BA%E8%AE%AE)
*   [总结](https://tendcode.com/subject/article/linux-oom/#%E6%80%BB%E7%BB%93)

![Image 1: image](https://tendcode.com/subject/article/linux-oom/)

[粤ICP备2024308668号](https://beian.miit.gov.cn/)网站已续航 7 年 93 天

Copyright©2018-2025[Hopetree](https://github.com/Hopetree "博客作者的Github").Powered by Django. [Sitemap](https://tendcode.com/sitemap.xml)

