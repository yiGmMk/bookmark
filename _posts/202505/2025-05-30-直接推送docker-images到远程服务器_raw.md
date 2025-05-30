---
layout: post
---
Title: Pushing Docker images to a remote host | Heitor's log

URL Source: https://heitorpb.github.io/bla/push-docker-img/

Markdown Content:
Today I had to ship some Docker images to a remote server and I was just too lazy to push to a registry, like Docker Hub. That would require me to log-in twice: once in my laptop and once in the remote server, that’s too much effort. I can SSH into the server, so why not just ship the images?

We can save an image as a tarball with the command `docker image save my_image:foo`. This will dump a tarball to the terminal, or we can save the output to a file with the `--output my_image.tar` flag. Note: this tarball is not compressed. You can compress with gzip for example: `docker image save my_image:foo | gzip > my_image.tar.gz`.

Docker can do the opposite as well: load an image from a tarball. The command is `docker image load`. This command expects the tarball from _stdin_, but we can also specify a file to read from: `docker image load --input my_image.tar`.

As both commands work with the same data format, we can combine them with a pipe: `docker image save my_image:foo | docker image load`, avoiding intermediate files.

Here enters a little trick: we can use SSH “between” the two commands, like a network pipe, to send the output of `docker image save` from my laptop to the input of `docker image load` in a remote server:

```
$ docker image save hello-world:latest | ssh user@server.com docker image load
Getting image source signatures
Copying blob sha256:63a41026379f4391a306242eb0b9f26dc3550d863b7fdbb97d899f6eb89efe72
Copying config sha256:74cc54e27dc41bb10dc4b2226072d469509f2f22f1a3ce74f4a59661a1d44602
Writing manifest to image destination
Loaded image: docker.io/library/hello-world:latest
```

We can also do the opposite: get the image from a remote server. The command just swaps where the SSH is: `ssh user@server.com docker image save hello-world:latest | docker image load`

I mentioned earlier that the tarballs exported are not compressed. You can compress them with `gzip`, or `xz`, and they just work. You can also use other compression formats if you also run the “uncompressor” on the target machine, for example: `docker image save foo | bzip2 | ssh user@host 'bunzip2 | docker image load'`.

Here I assumed you have access to Docker, either being root or root equivalent (if your user is in the `docker` group, this is dangerous) or running Docker in rootless mode (never seen anyone doing that though).

The good news is: Podman has the same commands and they work the same :) so:

*   `podman image save IMAGE | ssh user@server.com podman image load`
*   `podman image save IMAGE | gzip | ssh user@server.com podman image load`
*   `ssh user@server.com podman image save IMAGE | podman image load`
*   `ssh user@server.com 'podman image save IMAGE | gzip' | podman image load`

We can also use this `save | load` approach to send an image from Docker to Podman on the same machine. I have rootfull Docker and [rootless] Podman on my laptop and they don’t share the images. An image that Docker has is not available from Podman. But I can send and image from one to another: `podman image save IMAGE | sudo docker image load` and now Podman and Docker have the same image.

