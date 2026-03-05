from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms.task_forms import CreateTaskForm
from app.models.status import STATUS_LABELS
from app.services.task_service import create_task, get_user_tasks, delete_task
from app.models import Status, Priority

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/")
@login_required
def tasks():

    return render_template("tasks.html",
                           STATUS_LABELS=STATUS_LABELS,
                           Status=Status,
                           Priority=Priority,
                           tasks=get_user_tasks(user_id=current_user.id))


@tasks_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():

    if request.method == "POST":

        form = CreateTaskForm(request.form)
        if not form.success:
            for error in form.errors.values():
                flash(error, "error")
            return redirect(url_for("tasks.create"))

        result = create_task(
            user_id=current_user.id,
            title=form.title,
            description=form.description,
            due_date=form.due_date,
            status=form.status,
            priority=form.priority
        )
        if not result.success:
            for error in result.errors.values():
                flash(error, "error")
            return redirect(url_for("tasks.create"))

        flash("task successfully created!", "success")
        return redirect(url_for("tasks.tasks"))

    return render_template("create.html",
                           STATUS_LABELS=STATUS_LABELS,
                           Status=Status,
                           Priority=Priority)


@tasks_bp.route("/delete/<int:task_id>", methods=["POST"])
@login_required
def delete(task_id: int):

    result = delete_task(task_id=task_id, user_id=current_user.id)

    if not result.success:
        for error in result.errors.values():
            flash(error, "error")
        return redirect(url_for("tasks.tasks"))

    flash("successfully deleted", "success")
    return redirect(url_for("tasks.tasks"))
