---
layout: post
---
# Linux 系统 OOM 排查指南_Linux 笔记
- URL: [原文](https://tendcode.com/subject/article/linux-oom/)
- Added At: 2025-06-29 14:26:04
- [Link To Text](_posts/2025-06-29-linux-系统-oom-排查指南_linux-笔记_raw.md)

## TL;DR
Linux系统OOM排查主要通过查看日志（dmesg, journalctl, /var/log/messages, /var/log/syslog）确认OOM Killer是否启动，并分析被杀进程。需监控内存使用情况（包括历史和实时进程占用），利用`top`、`ps`等命令，关注内存飙升和高占用进程。`oom_score`可评估进程被kill风险。建议使用cgroups限制内存，并配置服务日志辅助分析。


## Summary
1.  **文章标题**：Linux 系统 OOM 排查指南

2.  **文章来源**：tendcode.com 网站

3.  **发布时间**：2025年4月29日

4.  **OOM简介**：
    *   定义：OOM (Out of Memory) 指 Linux 系统可用内存资源耗尽。
    *   触发条件：进程占用内存超过系统可用物理内存和交换空间。
    *   常见场景：系统负载过高、进程内存泄漏、系统内存资源不足。
    *   后果：触发 OOM Killer 机制，杀掉进程释放内存，可能导致服务中断、数据丢失。

5.  **查看系统日志**：
    *   **dmesg命令**：
        *   命令：`dmesg | grep -i "killed process"` 或 `dmesg | grep -i "out of memory"`
        *   作用：快速查看内核日志中是否有 OOM Kill 信息。
        *   输出示例：显示被 kill 的进程信息。
    *   **查看日志文件**：
        *   命令：`grep -i 'killed process' /var/log/messages` 或 `grep -i 'oom' /var/log/syslog`
        *   作用：查看系统级日志中历史 OOM 信息。
        *   日志文件路径：
            *   RHEL/CentOS：`/var/log/messages`
            *   Debian/Ubuntu：`/var/log/syslog`

6.  **使用journalctl**：
    *   适用系统：systemd 系统
    *   命令：`journalctl -k | grep -i 'killed process'`
    *   结合时间范围：`journalctl -k --since "1 hour ago" | grep -i 'oom'`

7.  **排查内存使用情况**：
    *   **查看内存使用历史**：
        *   工具：监控平台 (Prometheus + Grafana, Zabbix, Nagios)。
        *   关注指标：Memory usage, Cache, Swap usage, OOM Kill 指标。
        *   重点：关注是否有突发性内存飙升。
    *   **查看进程内存使用情况**：
        *   命令：`top`, `htop`, `ps aux --sort=-%mem | head -n 10`
        *   作用：实时/手动查看进程的内存使用情况。

8.  **查看OOM统计信息**：
    *   **查看进程OOM评分**：
        *   命令：`cat /proc/<pid>/oom_score`
        *   作用：检查进程被 OOM Kill 的风险（数值越高，被杀概率越大）。

9.  **其他建议**：
    *   `vm.panic_on_oom=1`：发生OOM时触发内核 panic（慎用，仅限高可靠系统）。
    *   使用 cgroups：限制容器或服务的内存使用，避免影响整个系统。
    *   服务日志：在被 OOM 的服务中设置日志，间接确认异常退出原因。

10. **总结表格**：

    | 方法 | 说明 |
    | --- | --- |
    | dmesg / journalctl | 快速查看内核日志中是否有 OOM Kill |
    | /var/log/messages / syslog | 系统级日志查看历史 OOM 信息 |
    | oom_score | 检查进程被 OOM Kill 的风险 |
    | 监控系统 | 排查内存异常变化的时段和趋势 |


