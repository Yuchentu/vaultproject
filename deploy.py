from flask import *

app = Flask(__name__)

@app.route('/test', methods = ['GET'])
def test():
	return 'This is working!'


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')