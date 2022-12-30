<!-- This page taken from https://github.com/eiskaltdcpp/icecult/wiki -->
# Setting up daemon
* Run the daemon once and kill it:
```bash
eiskaltdcpp-daemon
```
* It created it's default config files under `~/.eiskaltdc++`. You should add the following lines into `~/.eiskaltdc++/DCPlusPlus.xml` and restart the daemon. For multiple directories to share add multiple directory tags:
```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<DCPlusPlus>
  <Settings>
    <Nick>MyNickname</Nick>
    ...
  </Settings>
  <Share>
    <Directory Virtual="Name of share">/path/to/share/</Directory>
  </Share>
```
* Add your hub to `~/.eiskaltdc++/Favorites.xml` for auto connect:
```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Favorites>
  <Hubs>
    <Hub Name="Name of your hub" Connect="1" Description="" Nick="MyNickname" Password="" Server="adc://HubIP:HubPort" UserDescription="" Encoding="" ClientId="" ExternalIP="" OverrideId="0" UseInternetIp="0" DisableChat="0" Mode="0" SearchInterval="1"/>
  </Hubs>
  <Users/>
  <UserCommands/>
  <FavoriteDirs/>
</Favorites>
```
