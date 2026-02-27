from flask import render_template, Blueprint

from app.services.user_service import list_all_users

"""
home page routing
"""

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

#i just use this to have a quick look at the registered users, would not use in an actual application
@main_bp.route("/users")
def users():
    return list_all_users()