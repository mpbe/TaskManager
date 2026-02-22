from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms.auth_forms import LoginUserForm, RegisterUserForm
from app.services.auth_service import authenticate_user, register_user
from flask_login import login_user

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

        result = authenticate_user(username=form.username, password=form.password)

        if not result.success:
            for error in result.errors.values():
                flash(error, "error")
            return redirect(url_for("auth.login"))

        login_user(result.user)
        #change
        return redirect(url_for("main.index"))


    return render_template("login.html")

@auth_bp.route("/register", methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        form = RegisterUserForm(request.form)

        if not form.success:
            for error in form.errors.values():
                flash(error, "error")
            return redirect(url_for("auth.register"))

        result = register_user(username=form.username, email=form.email, password=form.password)

        if not result.success:
            for error in result.errors.values():
                flash(error, "error")
            return redirect(url_for("auth.register"))

        #change
        return redirect(url_for("main.index"))

    #change this later
    return render_template("register.html")