<!-- # Copyright (c) 2023 Nikita Beloglazov, Dmitry Markov -->
<!-- License: Mozilla Public License 2.0 -->
[![License: Mozilla Public License 2.0](https://img.shields.io/badge/License-Mozilla%20Public%20License%202.0-blueviolet.svg)](https://mozilla.org/en-US/MPL/2.0)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-success)](https://pylint.pycqa.org/en/latest/)
[![maintainer: NikitaBeloglazov](https://img.shields.io/badge/maintainer-.%E2%80%A2%C2%B0%E2%97%8F%E2%9D%A4%EF%B8%8F%20NikitaBeloglazov%20Software%20Foundation%20%E2%9D%A4%EF%B8%8F%E2%97%8F%C2%B0%E2%80%A2.-informational)](https://github.com/NikitaBeloglazov)
[![forkedFrom: eiskaltdcpp/icecult](https://img.shields.io/badge/forked%20from-eiskaltdcpp%2Ficecult-inactive)](https://github.com/eiskaltdcpp/icecult)

# icecult-reborn
Forked from [eiskaltdcpp/icecult](https://github.com/eiskaltdcpp/icecult).
Alternative webinterface for [eiskaltdcpp-daemon](https://github.com/eiskaltdcpp/eiskaltdcpp).

# Features:
* Connect to hubs
* Chat (History stored in Browser)
* Browse filelists of hub's users
* Download folders/files
* List of current/queued downloads
* Show Hash status and Upload/Download-Ratio
* Search on current server (thanks, [campbebj](https://github.com/eiskaltdcpp/icecult/pull/26))

### 🔽 Frontender HELP WANTED
Planned:
* Search sorting
* Optimize quering users on the current server
* Fix Bug, if the file name in the search is too long, the download button disappears beyond the visibility zone
* Search on all servers
* Optimize frontend (rewrite?)

# Screenshots
*needs to update
* Hubs: [*click*](https://raw.github.com/eiskaltdcpp/icecult/master/screens/icecult_hubs.png)
* Browse: [*click*](https://raw.github.com/eiskaltdcpp/icecult/master/screens/icecult_browse.png)
* Queue: [*click*](https://raw.github.com/eiskaltdcpp/icecult/master/screens/icecult_queue.png)

# Install
### Simple
Clone the repository to your local disk
```shell
git clone https://github.com/NikitaBeloglazov/icecult-reborn
```
Then install flask module
```shell
pip3 install flask
```
And then test it with the running daemon. If need, use Testing section below.
```shell
python3 redirect.py
```

### Setting up without package completely manually
```shell
git clone https://github.com:NikitaBeloglazov/icecult-reborn.git /tmp/icecult
cd /tmp/icecult
git checkout $VERSION
install -Dm 644  contrib/systemd/icecult.service /etc/systemd/system/icecult.service
install -Dm 644  contrib/systemd/icecult.env /etc/icecult.conf
install -Dm 644  contrib/systemd/icecult.sysusers /usr/lib/sysusers.d/system-user-icecult.conf
install -Dm 755  redirect.py /usr/bin/icecult
install -Dm 644 ./contrib/icecult_nginx_conf /etc/nginx/conf.d/icecult.conf
cp  app/* /var/lib/icecult/
systemd-sysusers /usr/lib/sysusers.d/system-user-valheim-server.conf
pip3 install flask
# edit env/cfg file as you need
systemctl enable --now icecult.service
cd ~
rm -rf /tmp/icecult
```

by default, the daemon runs as a separate user (`icecult`) who must also be present in the system.

If you need, [configure the daemon](/../../blob/main/SETTING_DAEMON.md) and configure server below

# Config

### Notation
*NAME_OF_VARIABLE = DEFAULT_VALUE

`DEMON_ADDRESS_AND_PORT = "127.0.0.0:3121"` — IP address and port where eiskaltdaemon jsonrpc interface is located

`WEB_ADDRESS = "0.0.0.0"` — IP address where the panel (icecult) will be located. Normally, editing this value is not necessary. If you don't know what it is, don't touch it.

`WEB_PORT = 8080` — Port where the panel (icecult) will be located. Useful with NAT servers
## Using env
Just write parameters before the main run command, like that:
```shell
DEMON_ADDRESS_AND_PORT="127.0.0.0:3121" WEB_ADDRESS="0.0.0.0" WEB_PORT="8080" python3 redirect.py
```
**If you don't know what env is and how to work with it** -> [*click*](https://web.archive.org/web/20221222050656/https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)

## Using systemd
**\*Relevant if you installed a ready-made package or installed completely manually, including unit for systemd**
* configure environments in env/cfg file `/etc/icecult.conf` with your parameters.
eg:
```ini
DEMON_ADDRESS_AND_PORT="127.0.0.1:3121"
WEB_ADDRESS="127.0.0.1"
WEB_PORT="8080"
```
* enable autostart & run service
```shell
systemctl enable --now icecult.service
```
* or restart service if it's already running
```shell
systemctl restart icecult.service
```

## Edit defauls in python file 
**\*Not recommended to use, your values may be erased during update**
* Open redirect.py file in text editor
* Search with keywords `# default`
* Replace default values to desired values

# Testing / Debug / Troubleshooting
* Try run `eiskaltdcpp-daemon --debug`
* If the connection with the demon is not happening, try running test_rpc.py, and look at the logs, if nothing happens at all, the redirect for some reason does not work at all
* You can also try specify `debug=True` in redirect.py (located at the end of the file)

# Contribution
* Patches are welcome!
* If you need to add extra library, then:
  * check the license of that library very carefully
  * check if that library is actively maintained (for fixing possible bugs in it)
  * try to find a usual CDN server hosting the file and only if you can't find one, copy source version of javascript file into this repo
* To speed up the process [write to maintainer](https://t.me/NikitaBeloglazov)

# License
* The main part of the code under [Mozilla Public License Version 2.0](/../../blob/main/LICENSE)
* Forked code [under MIT](https://github.com/eiskaltdcpp/icecult/blob/master/LICENSE)
* Some 3rd-party libraries [here](/../../tree/master/app/libs) licensed under MIT, too

# Changelog

=== FORKED ===

* 0.6.2:
  * bugfix: download of single files starting with "d"
  * bugfix: be more tolerant with hub's chat time formats [#23](https://github.com/eiskaltdcpp/icecult/pull/23)

* 0.6.1:
  * feature: wrap long chat messages [#21](https://github.com/eiskaltdcpp/icecult/pull/21)
  * feature: render urls in chat messages as links [#22](https://github.com/eiskaltdcpp/icecult/pull/22)

* 0.6.0:
  * feature: desktop notifications for chat messages [#18](https://github.com/eiskaltdcpp/icecult/pull/18)
  * feature: priorities for download queue [#17](https://github.com/eiskaltdcpp/icecult/pull/17) / [#19](https://github.com/eiskaltdcpp/icecult/pull/19)
  * feature: store enlargeable chat state [#20](https://github.com/eiskaltdcpp/icecult/pull/20)

* 0.5.2:
  * feature: enlargeable chat [#15](https://github.com/eiskaltdcpp/icecult/pull/15) / [#16](https://github.com/eiskaltdcpp/icecult/pull/16) (thx [@mmrose](https://github.com/mmrose))
  * feature: improved ui: auto scaling chat size window, better tooltips in user list, responsive navigation
  * bugfix: only partial filelist displayed in browse view

* 0.5.1:
  * feature: updated angular to 1.3.14
  * feature: added localstorage versioning
  * bugfix: proper html escaping of chat messages [#14](https://github.com/eiskaltdcpp/icecult/pull/14)

* 0.5.0:
  * feature: added settings tab
  * feature: enabled possibility to pause/resume hashing
  * feature: updated angular to 1.3.13 and bootstrap to 3.3.2
  * bugfix: another error in update check

* 0.4.1:
  * bugfix: error in update check

* 0.4.0:
  * feature: show available updates in statusbar

* 0.3.0:
  * bugfix: Chat text could be sent multiple times [#8](https://github.com/eiskaltdcpp/icecult/pull/8)
  * feature: Download queue size visible in status bar [#9](https://github.com/eiskaltdcpp/icecult/pull/9)
  * feature: Updated angular and bootstrap versions

* 0.2.1:
  * bugfix: Abort buttons in Download queue not functional [#7](https://github.com/eiskaltdcpp/icecult/pull/7)

* 0.2.0:
  * bugfix: Update of already downloaded filelist not possible [#5](https://github.com/eiskaltdcpp/icecult/pull/5)
  * bugfix: In mobile view Bootstrap's navbar collapse button without function [#4](https://github.com/eiskaltdcpp/icecult/pull/4)
  * feature: Sorting users in hub view [#3](https://github.com/eiskaltdcpp/icecult/pull/3)
  * feature: Show bandwidth in kBit/s [#2](https://github.com/eiskaltdcpp/icecult/pull/2)

* 0.1.1:
  * feature: added queue item details button to show more information
  * feature: show daemon and client version

* 0.0.1:
  * initial version
