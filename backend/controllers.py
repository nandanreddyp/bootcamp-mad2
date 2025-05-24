from functools import wraps

from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from models import db, User, Quote

from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})


def is_admin():
    try:
        current_user = User.query.get(get_jwt_identity())
        if current_user.role != 'admin':
            return False
        return True
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False
    
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            current_user = User.query.get(get_jwt_identity())
            if current_user.role != 'admin':
                return {"message": "Access denied"}, 403
        except Exception as e:
            print(f"Error checking admin status: {e}")
            return {"message": "Access denied"}, 403
        return f(*args, **kwargs)
    return decorated_function

class Users(Resource):

    @jwt_required()
    @admin_required
    def get(self, user_id=None):
        if user_id: # Get user by ID
            user = User.query.get(user_id)
            if not user:
                return {"message": "User not found"}, 404
            return {"message": "User found", "user": user.to_dict()}, 200
        else: # Get all users
            users = User.query.all()
            return jsonify({"message": "All users", "users": [user.to_dict() for user in users]})

    @admin_required
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
            return {"message": "Account Created, Login to continue!", "user": user.to_dict()}, 201
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {e}")
            return {"message": "Error creating user", "error": str(e)}, 500

    def put(self): # login
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            access_token = create_access_token(identity=user.id)
            user = user.to_dict()
            return {"message": "Login successful", "access_token": access_token, "user": user}, 200
        else:
            return {"message": "Invalid credentials"}, 401

    def delete(self): # logout
        # Deletes the user
        return {"message": "DELETE Registration"}

class Quotes(Resource):

    @jwt_required()
    @cache.cached(timeout=60, key_prefix='quotes', query_string=True)
    def get(self, quote_id=None):
        if quote_id:
            quote = Quote.query.get(quote_id)
            if not quote:
                return {"message": "Quote not found"}, 404
            return {"message": "Quote found", "quote": quote.to_dict()}
        import time
        quotes = Quote.query.all()
        # suppose there are so many quotes then it will take time to fetch all quotes
        time.sleep(12)  # Simulating delay for demonstration
        quotes = [quote.to_dict() for quote in quotes]
        return {"message": "GET Quotes", "quotes": quotes}
    
    @jwt_required()
    @admin_required
    def post(self, quote_id=None):
        text = request.json.get('text', "No text provided")
        quote = Quote(text=text)
        db.session.add(quote)
        db.session.commit()
        cache.delete('quotes')
        return {"message": "Quote created", "quote": quote.to_dict()}
    
    @jwt_required()
    @admin_required
    def put(self, quote_id=None):
        if not quote_id:
            return {"message": "Quote ID is required to update a quote"}, 400
        quote = Quote.query.get(quote_id)
        if not quote:
            return {"message": "Quote not found with given id"}, 404
        text = request.json.get('text', "No text provided")
        quote.text = text
        db.session.commit()
        cache.delete('quotes')
        return {"message": "Quote updated", "quote": quote.to_dict()}
    
    @jwt_required()
    @admin_required
    def delete(self, quote_id=None):
        if not quote_id:
            return {"message": "Quote ID is required to delete a quote"}, 400
        quote = Quote.query.get(quote_id)
        if not quote:
            return {"message": "Quote not found with given id"}, 404
        db.session.delete(quote)
        db.session.commit()
        cache.delete('quotes')
        return {"message": "Quote deleted"}, 200




class ExportCSV(Resource):
    def get(self):
        from celery_app import export_csv
        task = export_csv.delay()
        return {"message": "CSV export initiated, we will send you a mail!"}, 200

