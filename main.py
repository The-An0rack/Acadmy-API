from flask import Flask
from flask_restful import Api, Resource
from requests.api import put

import user_details

app = Flask(__name__)
api = Api(app)

class User(Resource):
   def get(self, email):
        obj = user_details.get_user_data(email)
        return obj

api.add_resource(User,"/profile/<string:email>")

if __name__ == "__main__":
    app.run(debug=True)
