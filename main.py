from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class dewashish(Resource):
   def get(self):
        return{"Name":"Dewashish Mehta","Email":"Dewmehta99@gmail.com","Goal":"GATE CS"}

api.add_resource(dewashish,"/profile/dew")

class kartik(Resource):
       def get(self):
        return{"Name":"Kartik Bhatt","Email":"bhattkartik@gmail.com","Goal":"GATE CS"}

api.add_resource(kartik,"/profile/kartik")




if __name__ == "__main__":
    app.run(debug=True)
