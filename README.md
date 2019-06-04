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

# Explanation

By default download RealTek application, but you can pass the name of
application you need through --app-name (the name of button on portal.nmbu.no)

By default the name of file is the name of application, you can pass any name
through --filename.