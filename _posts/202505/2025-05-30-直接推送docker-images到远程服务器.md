---
layout: post
---
# Pushing Docker images to a remote host | Heitor's log
- URL: [原文](https://heitorpb.github.io/bla/push-docker-img/)
- Added At: 2025-05-30 03:43:48
- [Link To Text](_posts/2025-05-30-直接推送docker-images到远程服务器_raw.md)

## TL;DR
本文介绍了一种无需镜像仓库，通过SSH管道直接在本地和远程服务器之间传输Docker或Podman镜像的方法。利用`docker image save`和`docker image load`命令，结合SSH管道和压缩工具，可以将镜像保存为tarball并传输，甚至可以在Docker和Podman之间互传镜像，极大地简化了镜像分发过程。该方法依赖于远程服务器的Docker访问权限和相应的解压工具。


## Summary
1.  **传输方式**：介绍了一种无需Docker Hub等镜像仓库，直接通过SSH传输Docker镜像到远程服务器的方法。

2.  **docker save命令**：
    *   可以将Docker镜像保存为tarball文件。
    *   命令：`docker image save my_image:foo`
    *   可以使用`--output my_image.tar`标志保存到文件。
    *   默认情况下，tarball文件未压缩。

3.  **gzip压缩**：
    *   可以使用gzip压缩tarball文件，以减小文件大小。
    *   命令：`docker image save my_image:foo | gzip > my_image.tar.gz`

4.  **docker load命令**：
    *   可以从tarball文件加载Docker镜像。
    *   命令：`docker image load`
    *   默认从_stdin_读取数据。
    *   可以使用`--input my_image.tar`标志从文件读取。

5.  **管道传输**：
    *   `docker image save`和`docker image load`可以结合使用管道符`|`，避免中间文件。
    *   命令：`docker image save my_image:foo | docker image load`

6.  **SSH管道**：
    *   利用SSH在本地和远程服务器之间建立管道，实现镜像传输。
    *   从本地推送到远程：`docker image save hello-world:latest | ssh user@server.com docker image load`
    *   从远程拉取到本地：`ssh user@server.com docker image save hello-world:latest | docker image load`

7.  **压缩传输**：
    *   支持压缩格式，例如gzip、xz和bzip2。
    *   需保证目标机器上存在对应的解压工具。
    *   示例：`docker image save foo | bzip2 | ssh user@host 'bunzip2 | docker image load'`

8.  **权限假设**：
    *   假设用户在远程服务器上有Docker访问权限（root用户或docker用户组成员）。

9.  **Podman支持**：
    *   Podman具有相同的命令并且工作方式相同，可以互换使用。
    *   `podman image save IMAGE | ssh user@server.com podman image load`
    *   `podman image save IMAGE | gzip | ssh user@server.com podman image load`
    *   `ssh user@server.com podman image save IMAGE | podman image load`
    *   `ssh user@server.com 'podman image save IMAGE | gzip' | podman image load`

10. **Docker与Podman互传**：
    *   即使在同一台机器上，rootful Docker和rootless Podman默认不共享镜像。
    *   可以通过`save | load`方式在Docker和Podman之间传输镜像。
    *   示例：`podman image save IMAGE | sudo docker image load`

