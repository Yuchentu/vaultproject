from flask import *
import os
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')
db = create_engine('postgres://npdvxwlrbkcwbk:02f49f9101fd6e9ed966c25f7ff3836e3644639e5a01a910dd92e7caa62a62fd@ec2-107-20-230-70.compute-1.amazonaws.com:5432/daqbaoap2pkdsk')

@app.route('/test', methods = ['GET'])
def test():
	return '<h1>Deployed</h1>'


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')