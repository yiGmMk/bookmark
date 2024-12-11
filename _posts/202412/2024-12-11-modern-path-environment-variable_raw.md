Title: Modern PATH environment variable

URL Source: https://blog.izissise.net/posts/env-path/

Published Time: 2024-10-08

Markdown Content:
The `PATH` environment variable is read by the shell or libc to find and execute programs, this is how the shell can find `/bin/ls` when `ls` is typed in a terminal.

[Shrink it](https://blog.izissise.net/posts/env-path/#shrink-it)
----------------------------------------------------------------

On Debian based desktop systems the default `PATH` variable look like this:

```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```

Much of this is not really necessary.

First, on modern systems, [`/{bin,sbin}/` directories are symlinks to `/usr/{bin,sbin}/`](https://wiki.debian.org/UsrMerge).

`/usr/local` has no use to me, if I compile/install software I'd rather they be put in the default locations[\[1\]](https://blog.izissise.net/posts/env-path/#fn-1).

Because sometimes I forgot to do `./configure --prefix=/usr` before compiling, I have setup `/usr/local` to symlink to `/usr` (`cd /usr && ln -s /usr local`). For software that are not found in public repositories and that should run as a daemon I use `/opt`.

This leaves a much shorter `PATH`:

```
PATH=/usr/sbin:/usr/bin:/usr/games
```

To go further, I remove `/usr/games` since I run GUI programs (like games) through their `.desktop` entries. These entries are located at [`${XDG_DATA_DIRS}/applications`](https://specifications.freedesktop.org/menu-spec/latest/paths.html).

And as of the year 2024 that's it, I'll use the root symlinks to have a little bit shorter string:

```
PATH=/sbin:/bin
```

Eventually, `/usr/sbin` might merge into `/usr/bin`, so only `/bin` will be needed.

[Expand it](https://blog.izissise.net/posts/env-path/#expand-it)
----------------------------------------------------------------

Setting `PATH` in `/etc/environment` is not the entire picture.

Once the shell is loaded, it also reads `/etc/profile` and `~/.profile`.

Modern programming environments, like Rust or Python, often add an entry to the `PATH`. However, I prefer to be explicit about what goes into the `PATH`, so I create symlinks:

```
$ file ~/bin ~/bin-rust ~/bin-py ~/bin-go ~/bin-js
~/bin:      directory
~/bin-rust: symbolic link to .cargo/bin
~/bin-py:   symbolic link to .local/bin
~/bin-go:   symbolic link to .golang/bin
~/bin-js:   symbolic link to .nvm/versions/node/v22.1.0/bin
```

I also want system binaries to take precedence on user one, so my `.profile` I make sure that `$PATH` comes first when reassigning:

```
# ...

# Hide default GOPATH
if [ -d "$HOME/.golang" ] ; then
    GOPATH="$HOME/.golang"
fi

# User's local bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$PATH:$HOME/bin"
fi

# RUST local bin if it exists
if [ -d "$HOME/bin-rust" ] ; then
    PATH="$PATH:$HOME/bin-rust"
fi

# Python local bin if it exists
if [ -d "$HOME/bin-py" ] ; then
    PATH="$PATH:$HOME/bin-py"
fi

# Golang local bin if it exists
if [ -d "$HOME/bin-go" ] ; then
    PATH="$PATH:$HOME/bin-go"
fi

# NodeJs local bin if it exists
if [ -d "$HOME/bin-js" ] ; then
    PATH="$PATH:$HOME/bin-js"
fi

export GOPATH
export PATH
```

With this setup, I can more easily verify if the correct binary is called.

* * *

1.  `man hier` for a description of system path. [↩](https://blog.izissise.net/posts/env-path/#fr-1-1)
