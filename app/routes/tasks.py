from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required

from app.forms.task_forms import CreateTaskForm

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/")
@login_required
def tasks():
    return render_template("tasks.html")


@tasks_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():

    if request.method == "POST":

        form = CreateTaskForm(request.form)
        if not form.success:
            for error in form.errors.values():
                flash(error, "error")
            return redirect("tasks.create")

        result = None


    return redirect(url_for("tasks.tasks"))