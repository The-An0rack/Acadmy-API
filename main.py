from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class profile(Resource):
   def get(self):
        return{"Name": "Dewashish Mehta","Email:": "Dewmehta99@gmail.com","Goal": "GATE CS")

api.add_resource(profile,"/profile")

if __name__ == "__main__":
    app.run(debug=True)
