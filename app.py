from flask import Flask
from captcha_controller import CaptchaController

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello world!"

@app.route('/captcha')
def captcha():
	captcha = CaptchaController()
	json = captcha.to_json()
	return json


if __name__ == '__main__':
	app.debug = True
	app.run('localhost', 3000, debug = True)