#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 Lars Kreisz
Copyright (c) 2022 Nikita Beloglazov (reason: forked)
License: The MIT License (MIT)
--
This script needs "flask" installed.
This code serving the webinterface
- runs locally, it serves the "app" folder via http(s) (control http(s) panel)
- requests to "/rpc" will be proxied to the 127.0.0.1:3121 (or another destination)
(eiskaltdaemon jsonrpc interface)
"""
# pylint: disable=line-too-long
import sys
import os
import requests
ENV_MESSAGE = 0 # see line 42
try:
    DEMON_ADDRESS_AND_PORT = os.environ['DEMON_ADDRESS_AND_PORT']
    # parse demon adress and port from env
except KeyError:
    ENV_MESSAGE += 1
    print("! Еnvironment setting \"DEMON_ADDRESS_AND_PORT\" not found. Using default.")
    DEMON_ADDRESS_AND_PORT = "127.0.0.0:3121" # default
print("-> DEMON_ADDRESS_AND_PORT = "+DEMON_ADDRESS_AND_PORT)

try:
    WEB_ADDRESS = os.environ['WEB_ADDRESS'] # parse web adress from env
except KeyError:
    ENV_MESSAGE += 1
    print("! Еnvironment setting \"WEB_ADDRESS\" not found. Using default.")
    WEB_ADDRESS = "0.0.0.0" # default
print("-> WEB_ADDRESS = "+WEB_ADDRESS)

try:
    WEB_PORT = int(os.environ['WEB_PORT']) # parse web port from env
except KeyError:
    ENV_MESSAGE += 1
    print("! Еnvironment setting \"WEB_PORT\" not found. Using default.")
    WEB_PORT = 8080 # default
print("-> WEB_PORT = "+str(WEB_PORT))

if ENV_MESSAGE == 3:
    print("!!! === No one environment settings found. Using standard settings that may not suit you.")
del ENV_MESSAGE

#DEMON_ADDRESS_AND_PORT = "127.0.0.0:3121"
#WEB_ADDRESS = "0.0.0.0"
#WEB_PORT    = 8080

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Verification
# Demon connectivity check
try:
    test = requests.post(f'http://{DEMON_ADDRESS_AND_PORT}/rpc',
        json={},
        timeout=30).text
except requests.exceptions.ConnectionError:
    print("!!! === Connect to daemon failed, please start daemon")
    sys.exit(1)
else:
    print("!!! === Connect to daemon successfully")
    print(test)
    del test

# = = =
# Dependencies check
try:
    from flask import Flask, request, send_from_directory
except ImportError:
    print("!!! === SKIPPED DEPENDENCIES\nInstall flask from your package manager or via pip \npip3 install flask")
    sys.exit(1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

app = Flask(__name__)

@app.route("/rpc/", methods = ['GET', 'POST'])


def proxy_to_rpc():
    """ Gives access to eiskaltdaemon jsonrpc interface """
    #print(request.json)
    #print("Redirect to port 3121")
    proxy_request = requests.post(
        f'http://{DEMON_ADDRESS_AND_PORT}/rpc',
        json=request.json,
        timeout=120).text
    #print("Giving the answer")
    return proxy_request

@app.route('/<path:filename>')
def upload_file(filename):
    """ Gives access to additional http page files (css files, etc) """
    return send_from_directory("app",
                            filename, as_attachment=False)

@app.route('/')
def index():
    """ Gives access to http of control panel """
    return send_from_directory("app",
                        "index.html", as_attachment=False)

if __name__ == '__main__':
    app.run(host=WEB_ADDRESS, port=WEB_PORT, debug=True)
