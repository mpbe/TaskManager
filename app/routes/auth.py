from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.forms.auth_forms import LoginUserForm

"""
routes related to logging in and registering users
"""

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods = ["GET", "POST"])
def login():

    if request.method == "POST":

        form = LoginUserForm(request.form)

        if not form.success:
            for error in form.errors.values():
                flash(error, "error")
            return redirect(url_for("auth.login"))


    return render_template("login.html")

@auth_bp.route("/register")
def register():
    return render_template("register.html")