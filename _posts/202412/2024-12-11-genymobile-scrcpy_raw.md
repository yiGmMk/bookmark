Title: GitHub - Genymobile/scrcpy: Display and control your Android device

URL Source: https://github.com/Genymobile/scrcpy

Markdown Content:
**This GitHub repo ([https://github.com/Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)) is the only official source for the project. Do not download releases from random websites, even if their name contains `scrcpy`.**

scrcpy (v3.1)
-------------

[](https://github.com/Genymobile/scrcpy#scrcpy-v31)

[![Image 20: scrcpy](https://github.com/Genymobile/scrcpy/raw/master/app/data/icon.svg)](https://github.com/Genymobile/scrcpy/blob/master/app/data/icon.svg)

_pronounced "**scr**een **c**o**py**"_

This application mirrors Android devices (video and audio) connected via USB or [over TCP/IP](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#tcpip-wireless), and allows to control the device with the keyboard and the mouse of the computer. It does not require any _root_ access. It works on _Linux_, _Windows_ and _macOS_.

[![Image 21: screenshot](https://github.com/Genymobile/scrcpy/raw/master/assets/screenshot-debian-600.jpg)](https://github.com/Genymobile/scrcpy/blob/master/assets/screenshot-debian-600.jpg)

It focuses on:

*   **lightness**: native, displays only the device screen
*   **performance**: 30~120fps, depending on the device
*   **quality**: 1920×1080 or above
*   **low latency**: [35~70ms](https://github.com/Genymobile/scrcpy/pull/646)
*   **low startup time**: ~1 second to display the first image
*   **non-intrusiveness**: nothing is left installed on the Android device
*   **user benefits**: no account, no ads, no internet required
*   **freedom**: free and open source software

Its features include:

*   [audio forwarding](https://github.com/Genymobile/scrcpy/blob/master/doc/audio.md) (Android 11+)
*   [recording](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md)
*   [virtual display](https://github.com/Genymobile/scrcpy/blob/master/doc/virtual_display.md)
*   mirroring with [Android device screen off](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md#turn-screen-off)
*   [copy-paste](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#copy-paste) in both directions
*   [configurable quality](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md)
*   [camera mirroring](https://github.com/Genymobile/scrcpy/blob/master/doc/camera.md) (Android 12+)
*   [mirroring as a webcam (V4L2)](https://github.com/Genymobile/scrcpy/blob/master/doc/v4l2.md) (Linux-only)
*   physical [keyboard](https://github.com/Genymobile/scrcpy/blob/master/doc/keyboard.md#physical-keyboard-simulation) and [mouse](https://github.com/Genymobile/scrcpy/blob/master/doc/mouse.md#physical-mouse-simulation) simulation (HID)
*   [gamepad](https://github.com/Genymobile/scrcpy/blob/master/doc/gamepad.md) support
*   [OTG mode](https://github.com/Genymobile/scrcpy/blob/master/doc/otg.md)
*   and more…

Prerequisites
-------------

[](https://github.com/Genymobile/scrcpy#prerequisites)

The Android device requires at least API 21 (Android 5.0).

[Audio forwarding](https://github.com/Genymobile/scrcpy/blob/master/doc/audio.md) is supported for API \>\= 30 (Android 11+).

Make sure you [enabled USB debugging](https://developer.android.com/studio/debug/dev-options#enable) on your device(s).

On some devices (especially Xiaomi), you might get the following error:

```
java.lang.SecurityException: Injecting input events requires the caller (or the source of the instrumentation, if any) to have the INJECT_EVENTS permission.
```

In that case, you need to enable [an additional option](https://github.com/Genymobile/scrcpy/issues/70#issuecomment-373286323) `USB debugging (Security Settings)` (this is an item different from `USB debugging`) to control it using a keyboard and mouse. Rebooting the device is necessary once this option is set.

Note that USB debugging is not required to run scrcpy in [OTG mode](https://github.com/Genymobile/scrcpy/blob/master/doc/otg.md).

Get the app
-----------

[](https://github.com/Genymobile/scrcpy#get-the-app)

*   [Linux](https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md)
*   [Windows](https://github.com/Genymobile/scrcpy/blob/master/doc/windows.md) (read [how to run](https://github.com/Genymobile/scrcpy/blob/master/doc/windows.md#run))
*   [macOS](https://github.com/Genymobile/scrcpy/blob/master/doc/macos.md)

Usage examples
--------------

[](https://github.com/Genymobile/scrcpy#usage-examples)

There are a lot of options, [documented](https://github.com/Genymobile/scrcpy#user-documentation) in separate pages. Here are just some common examples.

*   Capture the screen in H.265 (better quality), limit the size to 1920, limit the frame rate to 60fps, disable audio, and control the device by simulating a physical keyboard:
    
    scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --no-audio --keyboard=uhid
    scrcpy --video-codec=h265 -m1920 --max-fps=60 --no-audio -K  # short version
    
*   Start VLC in a new virtual display (separate from the device display):
    
    scrcpy --new-display=1920x1080 --start-app=org.videolan.vlc
    
*   Record the device camera in H.265 at 1920x1080 (and microphone) to an MP4 file:
    
    scrcpy --video-source=camera --video-codec=h265 --camera-size=1920x1080 --record=file.mp4
    
*   Capture the device front camera and expose it as a webcam on the computer (on Linux):
    
    scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=/dev/video2 --no-playback
    
*   Control the device without mirroring by simulating a physical keyboard and mouse (USB debugging not required):
    
*   Control the device using gamepad controllers plugged into the computer:
    
    scrcpy --gamepad=uhid
    scrcpy -G  # short version
    

User documentation
------------------

[](https://github.com/Genymobile/scrcpy#user-documentation)

The application provides a lot of features and configuration options. They are documented in the following pages:

*   [Connection](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md)
*   [Video](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md)
*   [Audio](https://github.com/Genymobile/scrcpy/blob/master/doc/audio.md)
*   [Control](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md)
*   [Keyboard](https://github.com/Genymobile/scrcpy/blob/master/doc/keyboard.md)
*   [Mouse](https://github.com/Genymobile/scrcpy/blob/master/doc/mouse.md)
*   [Gamepad](https://github.com/Genymobile/scrcpy/blob/master/doc/gamepad.md)
*   [Device](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md)
*   [Window](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md)
*   [Recording](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md)
*   [Virtual display](https://github.com/Genymobile/scrcpy/blob/master/doc/virtual_display.md)
*   [Tunnels](https://github.com/Genymobile/scrcpy/blob/master/doc/tunnels.md)
*   [OTG](https://github.com/Genymobile/scrcpy/blob/master/doc/otg.md)
*   [Camera](https://github.com/Genymobile/scrcpy/blob/master/doc/camera.md)
*   [Video4Linux](https://github.com/Genymobile/scrcpy/blob/master/doc/v4l2.md)
*   [Shortcuts](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md)

Resources
---------

[](https://github.com/Genymobile/scrcpy#resources)

*   [FAQ](https://github.com/Genymobile/scrcpy/blob/master/FAQ.md)
*   [Translations](https://github.com/Genymobile/scrcpy/wiki) (not necessarily up to date)
*   [Build instructions](https://github.com/Genymobile/scrcpy/blob/master/doc/build.md)
*   [Developers](https://github.com/Genymobile/scrcpy/blob/master/doc/develop.md)

Articles
--------

[](https://github.com/Genymobile/scrcpy#articles)

*   [Introducing scrcpy](https://blog.rom1v.com/2018/03/introducing-scrcpy/)
*   [Scrcpy now works wirelessly](https://www.genymotion.com/blog/open-source-project-scrcpy-now-works-wirelessly/)
*   [Scrcpy 2.0, with audio](https://blog.rom1v.com/2023/03/scrcpy-2-0-with-audio/)

Contact
-------

[](https://github.com/Genymobile/scrcpy#contact)

You can open an [issue](https://github.com/Genymobile/scrcpy/issues) for bug reports, feature requests or general questions.

For bug reports, please read the [FAQ](https://github.com/Genymobile/scrcpy/blob/master/FAQ.md) first, you might find a solution to your problem immediately.

You can also use:

*   Reddit: [`r/scrcpy`](https://www.reddit.com/r/scrcpy)
*   BlueSky: [`@scrcpy.bsky.social`](https://bsky.app/profile/scrcpy.bsky.social)
*   Twitter: [`@scrcpy_app`](https://twitter.com/scrcpy_app)

Donate
------

[](https://github.com/Genymobile/scrcpy#donate)

I'm [@rom1v](https://github.com/rom1v), the author and maintainer of _scrcpy_.

If you appreciate this application, you can [support my open source work](https://blog.rom1v.com/about/#support-my-open-source-work):

*   [GitHub Sponsors](https://github.com/sponsors/rom1v)
*   [Liberapay](https://liberapay.com/rom1v/)
*   [PayPal](https://paypal.me/rom2v)

Licence
-------

[](https://github.com/Genymobile/scrcpy#licence)

```
Copyright (C) 2018 Genymobile
Copyright (C) 2018-2024 Romain Vimont

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
