DEMON_ADDRESS_AND_PORT = "127.0.0.0:3121"

WEB_ADDRESS = "0.0.0.0"
WEB_PORT   = 8080

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

try:
	from flask import Flask, request, send_from_directory, render_template
except ImportError:
	print("!!! === SKIPPED DEPENDENCIES\nInstall flask: \npip3 install flask")
	exit()

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
