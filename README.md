# NMBU Remote RDP Downloader

Replacement for the manual downloading of RDP file from portal.nmbu.no
Mostly unuseful but saves your nervous and a tiny amount of time.
**When you will try to open .rdp file it will ask to write a password
with a strange username, just type in your NMBU password and enter**

### Requirements

Python 3
```
pip install requests
```

### Quick Reference

```
usage: download-remote-rdp.py [-h] [--app-name APP_NAME] [-f FILENAME]

Auto-downloader of remote desktop files for NMBU from portal.nmbu.no

optional arguments:
  -h, --help            show this help message and exit
  -app APP_NAME, --app-name APP_NAME
                        name of application (default=RealTek)
  -f FILENAME, --filename FILENAME
                        path to save .rdp file
  -l --only-link        prints link only (no saving file)
```

### Examples

```bash
# Downloads RealTek application with name RealTek.rdp
python download-remote-rdp.py
# The same
python download-remote-rdp.py --app-name RealTek --filename RealTek.rdp

# Downloads HomeOffice application with name HomeOffice.rdp
python download-remote-rdp.py --app-name HomeOffice
```

### Way to embed it in linux

Put nmbu-download-remote-rdp.py in `~/bin` directory (or whatever). Then
you can make an alias in `~/.bash_aliases` file.

```bash
# simple one
alias nmbu-remote="nmbu-download-remote-rdp -f ~/tmp/realtek/launch.rdp && xfreerdp ~/tmp/realtek/launch.rdp /dynamic-resolution"

# or if you want you can make alias with parameters
# which uses function [workaround](https://stackoverflow.com/questions/941338/how-to-pass-command-line-arguments-to-a-shell-alias)
# example of alias which takes as parameter folder to share with remote
alias nmbu-remote-share='function __nmbu_remote(){ nmbu-download-remote-rdp -f ~/tmp/realtek/launch.rdp; xfreerdp ~/tmp/realtek/launch.rdp /drive:shared,$1 /dynamic-resolution; };__nmbu_remote'

# or the last with which I stay: by default if shares $HOME, but you can
# also pass your path as optional argument
alias nmbu-remote='function __nmbu_remote(){ nmbu-download-remote-rdp -f ~/tmp/realtek/launch.rdp; xfreerdp ~/tmp/realtek/launch.rdp /drive:shared,$([ "$#" -eq 0 ] && echo "$HOME" || echo "$1") /dynamic-resolution; };__nmbu_remote'   
```

# Explanation

By default download RealTek application, but you can pass the name of
application you need through --app-name (the name of button on portal.nmbu.no)

By default the name of file is the name of application, you can pass any name
through --filename.