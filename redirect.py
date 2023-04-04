#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * Copyright (C) 2023 Nikita Beloglazov <nnikita.beloglazov@gmail.com>
 *
 * This file is part of NikitaBeloglazov/icecult-reborn.
 *
 * NikitaBeloglazov/icecult-reborn is free software; you can redistribute it and/or
 * modify it under the terms of the Mozilla Public License 2.0
 * published by the Mozilla Foundation.
 *
 * NikitaBeloglazov/icecult-reborn is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY.
 *
 * You should have received a copy of the Mozilla Public License 2.0
 * along with NikitaBeloglazov/icecult-reborn
 * If not, see https://mozilla.org/en-US/MPL/2.0.
"""

import os
env_message = 0 # see line 30
try:
	DEMON_ADDRESS_AND_PORT = os.environ['DEMON_ADDRESS_AND_PORT'] # parse demon adress and port from env
except:
	env_message += 1
	print("! Еnvironment setting \"DEMON_ADDRESS_AND_PORT\" not found. Using default.")
	DEMON_ADDRESS_AND_PORT = "127.0.0.0:3121" # default
print("-> DEMON_ADDRESS_AND_PORT = "+DEMON_ADDRESS_AND_PORT)

try:
	WEB_ADDRESS = os.environ['WEB_ADDRESS'] # parse web adress from env
except:
	env_message += 1
	print("! Еnvironment setting \"WEB_ADDRESS\" not found. Using default.")
	WEB_ADDRESS = "0.0.0.0" # default
print("-> WEB_ADDRESS = "+WEB_ADDRESS)

try:
	WEB_PORT = int(os.environ['WEB_PORT']) # parse web port from env
except:
	env_message += 1
	print("! Еnvironment setting \"WEB_PORT\" not found. Using default.")
	WEB_PORT = 8080 # default
print("-> WEB_PORT = "+str(WEB_PORT))

if env_message == 3:
	print("!!! === No one environment settings found. Using standard settings that may not suit you.")
del env_message

#DEMON_ADDRESS_AND_PORT = "127.0.0.0:3121"
#WEB_ADDRESS = "0.0.0.0"
#WEB_PORT    = 8080

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Verification
# Demon connectivity check
import requests
try:
	test = requests.post(f'http://{DEMON_ADDRESS_AND_PORT}/rpc', json={}).text
except:
	print("!!! === Connect to daemon failed, please start daemon")
	exit()
else:
	print("!!! === Connect to daemon successfully")
	print(test)
	del test

# = = =
# Dependencies check
try:
	from flask import Flask, request, send_from_directory, render_template
except ImportError:
	print("!!! === SKIPPED DEPENDENCIES\nInstall flask from your package manager or via pip: \npip3 install flask")
	exit()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

app = Flask(__name__)

@app.route("/rpc/", methods = ['GET', 'POST'])
def proxy_to_rpc():
	#print(request.json)
	print("Redirect to port 3121")
	proxy_request = requests.post(f'http://{DEMON_ADDRESS_AND_PORT}/rpc', json=request.json).text
	print("Giving the answer")
	return proxy_request

@app.route('/<path:filename>')
def upload_file(filename):
	return send_from_directory("app",
							filename, as_attachment=False)

@app.route('/')
def index():
	return send_from_directory("app",
						"index.html", as_attachment=False)

if __name__ == '__main__':
	app.run(host=WEB_ADDRESS, port=WEB_PORT, debug=True)
