[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg)](https://opensource.org/licenses/MIT)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-success)](https://pylint.pycqa.org/en/latest/)
[![author: NikitaBeloglazov](https://img.shields.io/badge/author-.%E2%80%A2%C2%B0%E2%97%8F%E2%9D%A4%EF%B8%8F%20NikitaBeloglazov%20Software%20Foundation%20%E2%9D%A4%EF%B8%8F%E2%97%8F%C2%B0%E2%80%A2.-informational)](https://github.com/NikitaBeloglazov)
[![forkedFrom: eiskaltdcpp/icecult](https://img.shields.io/badge/forked%20from-eiskaltdcpp%2Ficecult-inactive)](https://github.com/eiskaltdcpp/icecult)

# icecult-reborn
Forked from [eiskaltdcpp/icecult](https://github.com/eiskaltdcpp/icecult).
Alternative webinterface for [eiskaltdcpp-daemon](https://github.com/eiskaltdcpp/eiskaltdcpp).

Features:
* Connect to hubs
* Chat (History stored in Browser)
* Browse filelists of hub's users
* Download folders/files
* List of current/queued downloads
* Show Hash status and Upload/Download-Ratio
* Search on current server (thanks, [campbebj](https://github.com/eiskaltdcpp/icecult/pull/26))

Planned:
* Search sorting
* Search on all servers
* Optimize quering users on the current server
* Optimize frontend (rewrite?)

# Screenshots
*needs to update
* Hubs: [*click*](https://raw.github.com/eiskaltdcpp/icecult/master/screens/icecult_hubs.png)
* Browse: [*click*](https://raw.github.com/eiskaltdcpp/icecult/master/screens/icecult_browse.png)
* Queue: [*click*](https://raw.github.com/eiskaltdcpp/icecult/master/screens/icecult_queue.png)

# Install
Clone the repository to your local disk
```
git clone https://github.com/NikitaBeloglazov/icecult-reborn
```
Then install flask module
```
pip3 install flask
```
And then test it with the running daemon. If need, use Testing section below.
```
python3 redirect.py
```
### Setting up systemd
*WORKING

If you need, [configure the daemon](/../../blob/master/SETTING_DAEMON.md) and configure server below

# Config

### Notation
*NAME_OF_VARIABLE = DEFAULT_VALUE

`DEMON_ADDRESS_AND_PORT = "127.0.0.0:3121"` — IP address and port where eiskaltdaemon jsonrpc interface is located

`WEB_ADDRESS = "0.0.0.0"` — IP address where the panel (icecult) will be located. Normally, editing this value is not necessary. If you don't know what it is, don't touch it.

`WEB_PORT = 8080` — Port where the panel (icecult) will be located. Useful with NAT servers
## Using env
Just write parameters before the main run command, like that:
```
DEMON_ADDRESS_AND_PORT="127.0.0.0:3121" WEB_ADDRESS="0.0.0.0" WEB_PORT="8080" python3 redirect.py
```
**If you don't know what env is and how to work with it** -> [*click*](https://web.archive.org/web/20221222050656/https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)

## Using systemd
*WORKING
## Edit defauls in python file 
**\*Not recommended to use, your values may be erased during update**
* Open redirect.py file in text editor
* Search with keywords `# default`
* Replace default values to desired values

# Contribution
* Patches are welcome!
* If you need to add extra library, then:
  * check the license of that library very carefully
  * check if that library is actively maintained (for fixing possible bugs in it)
  * try to find a usual CDN server hosting the file and only if you can't find one, copy source version of javascript file into this repo
* To speed up the process [write to maintainer](https://t.me/NikitaBeloglazov)

# License
* [MIT license](/../../blob/master/LICENSE)
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
