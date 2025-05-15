from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

# initialize the database
from models import db
db.init_app(app)

# add the api routes
from controllers import Api, Authentication, Users
api = Api(app)

api.add_resource(Authentication, '/api/auth')
api.add_resource(Users, '/api/users', '/api/users/<int:user_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)