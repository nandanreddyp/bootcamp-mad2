from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource

from models import db, User

class Users(Resource):
    def get(self, user_id=None):
        if user_id: # Get user by ID
            user = User.query.get(user_id)
            if not user:
                return {"message": "User not found"}, 404
            return {"message": "User found", "user": user.to_dict()}, 200
        else: # Get all users
            users = User.query.all()
            return jsonify({"message": "All users", "users": [user.to_dict() for user in users]})

    def put(self, user_id): # edit user
        try:
            print(user_id)
            user = User.query.get(user_id)
            if not user:
                return {"message": "User not found"}, 404
            user.name = request.json.get('name', user.name)
            user.email = request.json.get('email', user.email)
            db.session.commit()
            return {"message": "User updated", "user": user.to_dict()}, 200
        except Exception as e:
            db.session.rollback()
            print(f"Error updating user: {e}")
            return {"message": "Error updating user", "error": str(e)}, 500
        
    def delete(self, user_id): # delete user
        try:
            user = User.query.get(user_id)
            if not user:
                return {"message": "User not found"}, 404
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted"}, 200
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting user: {e}")
            return {"message": "Error deleting user", "error": str(e)}, 500
    
class Authentication(Resource):
    def get(self):
        email = request.args.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            return {"message": "User exists", "user": user.to_dict()}, 200
        else:
            return {"message": "User does not exist"}, 404
        
    def post(self): # registration
        try:
            email = request.json.get('email')
            if User.query.filter_by(email=email).first():
                return {"message": "User already exists"}, 400
            user = User(
                name=request.json.get('name'),
                email=request.json.get('email'),
                password=request.json.get('password')
            )
            db.session.add(user)
            db.session.commit()
            return {"message": "User created", "user": user.to_dict()}, 201
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {e}")
            return {"message": "Error creating user", "error": str(e)}, 500

    def put(self): # login
        # Updates the user
        return jsonify({"message": "PUT Registration"})

    def delete(self): # logout
        # Deletes the user
        return jsonify({"message": "DELETE Registration"})




