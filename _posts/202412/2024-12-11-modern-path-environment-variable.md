---
layout: post
---
# Modern PATH environment variable
- URL: https://blog.izissise.net/posts/env-path/
- Added At: 2024-12-11 03:38:06
- [Link To Text](2024-12-11-modern-path-environment-variable_raw.md)

## TL;DR
PATH环境变量是shell或libc读取以找到和执行程序的变量。优化PATH环境变量可以提高系统性能。优化步骤包括移除不必要的目录，如`/{bin,sbin}/`和`/usr/local`目录，移除`/usr/games`目录。优化后的PATH变量可以简化为`PATH=/usr/sbin:/usr/bin:/usr/games`或`PATH=/sbin:/bin`。此外，可以通过设置PATH环境变量、shell读取配置文件、显式添加PATH条目和确保系统二进制文件优先来扩展PATH环境变量。

## Summary
1. **PATH环境变量简介**：PATH环境变量是shell或libc读取以找到和执行程序的变量，shell可以通过它找到`/bin/ls`当在终端中输入`ls`时。

2. **PATH环境变量的优化**：
   - **Debian系统默认PATH变量**：PATH变量通常包含多个目录，如`/usr/local/sbin`、`/usr/local/bin`、`/usr/sbin`、`/usr/bin`、`/sbin`、`/bin`、`/usr/games`、`/usr/local/games`。
   - **优化步骤**：
     - **移除不必要的目录**：在现代系统中，`/{bin,sbin}/`目录是`/usr/{bin,sbin}/`的符号链接，因此可以移除。
     - **移除`/usr/local`目录**：如果编译或安装软件，建议将其安装在默认位置，而不是`/usr/local`目录。
     - **移除`/usr/games`目录**：如果使用`.desktop`条目运行GUI程序（如游戏），则可以移除该目录。
   - **优化后的PATH变量**：PATH变量可以简化为`PATH=/usr/sbin:/usr/bin:/usr/games`，甚至进一步简化为`PATH=/sbin:/bin`。

3. **PATH环境变量的扩展**：
   - **设置PATH环境变量**：可以在`/etc/environment`中设置PATH环境变量，但这不是全部。
   - **shell读取配置文件**：shell会读取`/etc/profile`和`~/.profile`配置文件。
   - **显式添加PATH条目**：可以显式添加PATH条目，例如通过创建符号链接。
   - **确保系统二进制文件优先**：可以通过在`.profile`文件中重新赋值PATH变量来确保系统二进制文件优先于用户二进制文件。

4. **示例配置**：
   - **创建符号链接**：可以创建符号链接，如`~/bin`、`~/bin-rust`、`~/bin-py`、`~/bin-go`、`~/bin-js`，指向相应的二进制文件目录。
   - **配置`.profile`文件**：可以在`.profile`文件中添加代码来检查和添加PATH条目。
