from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response

app = Flask(__name__)
api = Api(app)


class Demo(Resource):
    def get(self):
        return make_response(jsonify({"message": "default endpoint"}), 200)


api.add_resource(Demo, "/")
