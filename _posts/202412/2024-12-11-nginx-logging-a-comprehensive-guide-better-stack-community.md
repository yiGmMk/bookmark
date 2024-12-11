# Nginx Logging: A Comprehensive Guide | Better Stack Community
- URL: https://betterstack.com/community/guides/logging/how-to-view-and-configure-nginx-access-and-error-logs/
- Added At: 2024-12-11 08:58:44
- [Link To Text](2024-12-11-nginx-logging-a-comprehensive-guide-better-stack-community_raw.md)

## TL;DR
本文是一篇关于 Nginx 日志的指南，介绍了如何使用 Docker 运行 Nginx，配置 Nginx 日志，查看 Nginx 日志，解析 Nginx 日志，并展示了 Nginx 日志的格式。

## Summary
**Nginx 日志指南**
================

### **Nginx 日志简介**

Nginx 是一个流行的 Web 服务器，它记录了大量的数据，包括客户端交互、系统事件和错误信息。然而，这些数据的潜力只有通过正确的配置、管理和分析才能被充分发挥出来。

### **本文目标**

本文将教你如何有效地自定义 Nginx 日志，以获得更好的可视性和控制你的 Web 服务器和代理。

### **前提条件**

*   基本的命令行技能
*   一个 Linux 系统，包括一个非 root 用户具有 sudo 权限
*   最近版本的 Docker 安装在你的系统上

### **步骤 1：使用 Docker 运行 Nginx**

使用官方的 Docker 镜像是开始使用 Nginx 的最简单方式。它简化了设置过程，并确保了在不同系统上的可重现性。

### **步骤 2：配置 Nginx 日志**

Nginx 日志可以通过配置文件进行自定义。配置文件通常位于 `/etc/nginx/nginx.conf`。

### **步骤 3：查看 Nginx 日志**

Nginx 日志可以通过 `docker logs` 命令进行查看。

### **步骤 4：解析 Nginx 日志**

Nginx 日志可以通过 `jq` 命令进行解析。

### **Nginx 日志格式**

Nginx 日志格式通常如下：

```
{
  "container_created_at": "2024-08-08T08:59:06.052457248Z",
  "container_id": "0f17a23cef07616df8cf4f698664e8b9f2c62daaff75bbfc77d750f797eb06c5",
  "container_name": "nginx-server",
  "context": {
    "cid": 1,
    "client": "172.24.0.1",
    "host": "localhost",
    "pid": 23,
    "request": "GET /favicon.ico HTTP/1.1",
    "server": "localhost",
    "severity": "error",
    "tid": 23,
    "timestamp": "2024-08-08T16:37:59Z"
  },
  "host": "3d0ebf54b0eb",
  "image": "nginx:alpine",
  "label": {
    "com.docker.compose.config-hash": "b27d7c9cd09c4f82e419ac408790cbea8ea31a8102d37160b93b318cb4f18cc6",
    "com.docker.compose.container-number": "1",
    "com.docker.compose.depends_on": "",
    "com.docker.compose.image": "sha256:1ae23480369fa4139f6dec668d7a5a941b56ea174e9cf75e09771988fe621c95",
    "com.docker.compose.oneoff": "False",
    "com.docker.compose.project": "nginx-logging-tutorial",
    "com.docker.compose.project.config_files": "/home/ayo/dev/betterstack/demo/nginx-docker/docker-compose.yml",
    "com.docker.compose.project.working_dir": "/home/ayo/dev/betterstack/demo/nginx-docker",
    "com.docker.compose.service": "nginx",
    "com.docker.compose.version": "2.29.1",
    "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
  },
  "message": "open() \"/usr/share/nginx/html/favicon.ico\" failed (2: No such file or directory)",
  "source_type": "docker_logs",
  "stream": "stderr",
  "timestamp": "2024-08-08T16:37:59.012"
}
```

### **总结**

本文介绍了如何使用 Docker 运行 Nginx，配置 Nginx 日志，查看 Nginx 日志，解析 Nginx 日志。同时，也介绍了 Nginx 日志格式。
