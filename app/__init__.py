from flask import Flask
from app.routes.auth import auth_bp
from app.routes.main import main_bp
from config import Config
from app.extensions import db, login_manager
from app.models import User

"""
here i am setting up the main Flask application, and the database tables that will
be created (if they dont exist) on application run

i have also registered the blueprints that will be used to manage my routes, and
attached any prefixes they may need
"""

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    #import models here for db tables when created
    #register routes here when created
    #register the blueprints here when routes are created - and add prefixes here

    with app.app_context():
        db.create_all()

    return app