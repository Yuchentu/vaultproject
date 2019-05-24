from flask import *

app = Flask(__name__)

@app.route('/test', methods = ['GET'])
def test():
	return '<h1>Deployed</h1>'


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')