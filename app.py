from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

CORS(app)

class Authentication(Resource):
    def get(self):
        # Check if the user exists
        return jsonify({"message": "GET Registration"})

    def post(self):
        # Creates a new user
        return jsonify({"message": "POST Registration"})

    def put(self):
        # Updates the user
        return jsonify({"message": "PUT Registration"})

    def delete(self):
        # Deletes the user
        return jsonify({"message": "DELETE Registration"})
    
api.add_resource(Authentication, '/api/auth')



if __name__ == '__main__':
    app.run(debug=True)