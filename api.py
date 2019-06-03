from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


users = [
	{
		"email" : "xyz1@gmail.com",
		"password" : "123"
	},
	{
		"email" : "xyz2@gmail.com",
		"password" : "123"
	},
	{
		"email" : "xyz3@gmail.com",
		"password" : "123"
	}
]


class User(Resource):

	def get(self, email):
		for user in users:
			if(email == user["email"]):
				return user, 200
		return "User not found", 404
	def post(self, email):
		parser = reqprase.RequestParser()
		parser.add_argument("password")
		args = parser.parse_args()

		for user in users:
			if(email == user["email"]):
				return "User already exists", 400

		user = {"email" : email, "password" : args["password"]}
		users.append(user)
		return user, 201

	def delete(self, email):
		global users
		users = [user for user in users if user["email"] != email]
		return None, 200

api.add_resource(User, "/user/<string:email>")
app.run(debug=True)