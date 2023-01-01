#!/usr/bin/env python3
# coding=utf-8
from flask import Flask, request

app = Flask(__name__)

@app.route("/rpc", methods = ['POST'])
def hello_world():
	print(request.json)
	print("Giving [TEST RPC] OK")
	return "[TEST RPC] OK"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3121)
