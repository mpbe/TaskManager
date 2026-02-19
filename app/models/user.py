from app import db
from flask_login import UserMixin

"""
this is the User model and represents an authenticated user. it is a table in the DB
"""

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    hashed_password = db.Column(db.String(200), nullable=False)