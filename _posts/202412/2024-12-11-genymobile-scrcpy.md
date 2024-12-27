---
layout: post
---

# Genymobile/scrcpy
- URL: [原文](https://github.com/Genymobile/scrcpy)
- Added At: 2024-12-11 09:38:37
- [Link To Text](_posts/2024-12-11-genymobile-scrcpy_raw.md)

## TL;DR
scrcpy 是一个开源项目，允许用户通过 USB 或 TCP/IP 连接将 Android 设备的屏幕镜像到电脑上，并可以使用电脑的键盘和鼠标控制 Android 设备。它具有轻量级、高性能、高质量、低延迟、快速启动、非侵入性、用户利益和自由等特点。

## Summary
1. **项目简介**：scrcpy 是一个开源项目，允许用户通过 USB 或 TCP/IP 连接将 Android 设备的屏幕镜像到电脑上，并可以使用电脑的键盘和鼠标控制 Android 设备。

2. **特点**：
   - **轻量级**：native，仅显示设备屏幕
   - **高性能**：30~120fps，取决于设备
   - **高质量**：1920×1080 或以上
   - **低延迟**：35~70ms
   - **快速启动**：约 1 秒显示第一帧
   - **非侵入性**：不在 Android 设备上安装任何内容
   - **用户利益**：无需账号、无广告、无需互联网
   - **自由**：免费开源软件

3. **功能**：
   - **音频转发**（Android 11+）
   - **录制**
   - **虚拟显示**
   - **镜像 Android 设备屏幕关闭**
   - **复制粘贴**（双向）
   - **可配置质量**
   - **摄像头镜像**（Android 12+）
   - **镜像为网络摄像头（V4L2）**（仅限 Linux）
   - **物理键盘和鼠标模拟**（HID）
   - **游戏手柄支持**
   - **OTG 模式**
   - **更多功能**

4. **前提条件**：
   - Android 设备需要至少 API 21（Android 5.0）
   - 音频转发需要 API >= 30（Android 11+）
   - 需要在设备上启用 USB 调试

5. **获取应用**：
   - **Linux**：[文档](https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md)
   - **Windows**：[文档](https://github.com/Genymobile/scrcpy/blob/master/doc/windows.md)
   - **macOS**：[文档](https://github.com/Genymobile/scrcpy/blob/master/doc/macos.md)

6. **使用示例**：
   - 捕获屏幕并限制大小和帧率
   - 启动 VLC 在新虚拟显示上
   - 录制设备摄像头
   - 将设备前摄像头作为网络摄像头
   - 使用游戏手柄控制设备

7. **用户文档**：
   - [连接](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md)
   - [视频](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md)
   - [音频](https://github.com/Genymobile/scrcpy/blob/master/doc/audio.md)
   - [控制](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md)
   - [键盘](https://github.com/Genymobile/scrcpy/blob/master/doc/keyboard.md)
   - [鼠标](https://github.com/Genymobile/scrcpy/blob/master/doc/mouse.md)
   - [游戏手柄](https://github.com/Genymobile/scrcpy/blob/master/doc/gamepad.md)
   - [设备](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md)
   - [窗口](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md)
   - [录制](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md)
   - [虚拟显示](https://github.com/Genymobile/scrcpy/blob/master/doc/virtual_display.md)
   - [隧道](https://github.com/Genymobile/scrcpy/blob/master/doc/tunnels.md)
   - [OTG](https://github.com/Genymobile/scrcpy/blob/master/doc/otg.md)
   - [摄像头](https://github.com/Genymobile/scrcpy/blob/master/doc/camera.md)
   - [Video4Linux](https://github.com/Genymobile/scrcpy/blob/master/doc/v4l2.md)
   - [快捷键](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md)

8. **资源**：
   - [FAQ](https://github.com/Genymobile/scrcpy/blob/master/FAQ.md)
   - [翻译](https://github.com/Genymobile/scrcpy/wiki)
   - [构建指南](https://github.com/Genymobile/scrcpy/blob/master/doc/build.md)
   - [开发者](https://github.com/Genymobile/scrcpy/blob/master/doc/develop.md)

9. **文章**：
   - [介绍 scrcpy](https://blog.rom1v.com/2018/03/introducing-scrcpy/)
   - [scrcpy 现在支持无线连接](https://www.genymotion.com/blog/open-source-project-scrcpy-now-works-wirelessly/)
   - [scrcpy 2.0，带有音频](https://blog.rom1v.com/2023/03/scrcpy-2-0-with-audio/)

10. **联系**：
    - [问题](https://github.com/Genymobile/scrcpy/issues)
    - [Reddit](https://www.reddit.com/r/scrcpy)
    - [BlueSky](https://bsky.app/profile/scrcpy.bsky.social)
    - [Twitter](https://twitter.com/scrcpy_app)

11. **捐赠**：
    - [GitHub 赞助](https://github.com/sponsors/rom1v)
    - [Liberapay](https://liberapay.com/rom1v/)
    - [PayPal](https://paypal.me/rom2v)

12. **许可**：Apache License, Version 2.0
