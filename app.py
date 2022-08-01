from flask import Flask
from flask_restful import Resource, Api
#create my application
app = Flask(__name__)
#create my api
api = Api(app)

class sendMessage(Resource):
	def get(self):
		return {"message":"Message from container1"}

api.add_resource(sendMessage, '/')
#running my app attention 0.0.0.0 to run address of container
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
