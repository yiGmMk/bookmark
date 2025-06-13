---
layout: post
---
# GitHub - theopfr/somo: A human-friendly alternative to netstat for socket and port monitoring on Linux.
- URL: [原文](https://github.com/theopfr/somo)
- Added At: 2025-06-13 07:14:10
- [Link To Text](_posts/2025-06-13-theopfr-somo_raw.md)

## TL;DR
`somo`是一款更友好的Linux套接字和端口监控工具，旨在替代`netstat`。它提供表格化输出、强大的过滤功能和交互式进程管理。通过`cargo install somo`或`.deb`包安装后，可以使用简洁的命令和选项，如`somo -l`，快速查找特定连接并结束进程，例如`somo --program postgres -k`。项目使用MIT许可证，主要由Rust编写。


## Summary
以下是对GitHub上的`theopfr/somo`项目的总结：

1. **项目简介**: `somo` 是一个在Linux系统上用于监控套接字和端口的工具，旨在提供比 `netstat` 更人性化的替代方案。

2. **核心特性**:
   - **用户友好**: 通过表格视图展示信息，更易于阅读。
   - **可过滤性**: 提供多种过滤选项，方便用户查找特定连接。
   - **进程管理**: 允许交互式地结束进程。
   - **命令简化**: 提供了比 `netstat` 更简洁的命令格式，例如 `somo -l` 替代 `netstat -tulpn`。

3. **安装方式**:
   - **Debian**: 下载最新的 `.deb` 文件进行安装。
   - **crates.io**: 使用 `cargo install somo` 命令安装。
      - **sudo权限**: 建议创建符号链接，以便以root权限运行 `somo`，从而查看所有进程和端口。

4. **使用方式**:
   - **基本命令**: 直接运行 `sudo somo`。
   - **过滤选项**:
     - `--proto`: 按照TCP或UDP协议过滤。
     - `--port, -p`: 按照本地端口过滤。
     - `--remote-port`: 按照远程端口过滤。
     - `--ip`: 按照远程IP地址过滤。
     - `--program`: 按照客户端程序名称过滤。
     - `--pid, -p`: 按照进程ID过滤。
     - `--open, -o`: 过滤开放的连接。
     - `--listen, -l`: 过滤监听的连接。
     - `--exclude-ipv6`: 排除IPv6连接。
   - **进程结束**: 使用 `--kill, -k` 标志进行交互式进程选择并结束。
     - **结合过滤**: 可以同时使用过滤选项和结束进程标志，例如 `somo --program postgres -k`。

5. **项目信息**:
   - **License**: 使用 MIT License。
   - **Stars**: 755
   - **Forks**: 20
   - **Watchers**: 4
   - **Releases**: 2 (最新版本为1.0.0)
   - **Contributors**: 3 (theopfr, aptypp, robinhutty)
   - **Languages**: 主要使用Rust (100%)。

