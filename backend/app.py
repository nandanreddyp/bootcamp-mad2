from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from flask_jwt_extended import JWTManager

# create the Flask application and configure it
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configure JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['JWT_VERIFY_SUB'] = False
jwt = JWTManager(app)

# enable CORS for all routes
CORS(app)

# initialize the database
from models import db, User
db.init_app(app)

# add the api routes
from controllers import Api, Authentication, Users, Quotes, ExportCSV
api = Api(app)

api.add_resource(Authentication, '/api/auth')
api.add_resource(Users, '/api/users', '/api/users/<int:user_id>')
api.add_resource(Quotes, '/api/quotes', '/api/quotes/<int:quote_id>')
api.add_resource(ExportCSV, '/api/export_csv')


# running the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
        if not User.query.filter_by(email='admin@gmail.com').first():
            admin = User(
                name='Admin',
                email='admin@gmail.com',
                password='admin',
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin user created\nWith email: admin@gmail.com and password: admin")
    app.run(debug=True)
