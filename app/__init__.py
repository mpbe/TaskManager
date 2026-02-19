from flask import Flask
from config import Config
from app.extensions import db, login_manager

"""
here i am setting up the main Flask application, and the database tables that will
be created (if they dont exist) on application run
"""

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    #TODO import models here for db tables when created
    #TODO register routes here when created
    #TODO register the blueprints here when routes are created - and add prefixes here

    #uncomment this when you have tables to make
    # with app.app_context():
    #     db.create_all()

    return app