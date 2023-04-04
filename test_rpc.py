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

from flask import Flask, request

app = Flask(__name__)

@app.route("/rpc", methods = ['POST'])
def hello_world():
	print(request.json)
	print("Giving [TEST RPC] OK")
	return "[TEST RPC] OK"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3121)
