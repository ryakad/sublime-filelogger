Sublime FileLogger
==================

Sublime file logger is a simple flat file logger that assists in tracking
where you are spending your time working in sublime.

Installation
------------

To install you can simply clone into your packages directory.

```bash
cd /path/to/sublime/Packages
git clone https://github.com/ryakad/sublime-filelogger.git FileLogger
```

For access to the wl and cwl functions you can simply source it from your
~/.bashrc. Assuming you are still in the above directory run the following
command.

```bash
cd FileLogger
echo ". \"$(echo $PWD)/bin/functions.sh\"" >> ~/.bashrc
```

Now to view your work log you can simple run the `wl` command from your
terminal. If you only want to see the last 10 entries you can run `wl 10`.
