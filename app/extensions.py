from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

"""
here i am setting up SQLAlchemy and my Flask login
"""

db = SQLAlchemy()
login_manager = LoginManager()
#the page that the user will be taken to if user is not logged in
login_manager.login_view="auth.login"
#user will be shown the following message
login_manager.login_message="please log in to access"
login_manager.login_message_category="warning"


