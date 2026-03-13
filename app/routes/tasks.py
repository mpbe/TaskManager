from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms.task_forms import CreateTaskForm, UpdateTaskForm
from app.models.priority import PRIORITY_COLOURS
from app.models.status import STATUS_LABELS
from app.services.task_service import create_task, get_user_tasks, delete_task, update_task, get_task_by_id, \
    complete_task
from app.models import Status, Priority, Task

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/")
@login_required
def tasks():

    page = request.args.get("page", 1, type=int)
    search_term = request.args.get("search", "").strip()
    query = Task.query.filter_by(user_id=current_user.id)

    if search_term:
        query = query.filter(
            Task.title.ilike(f"%{search_term}%") |
            Task.description.ilike(f"%{search_term}%")
        )
    query = query.order_by(Task.id.asc())
    pagination = query.paginate(page=page, per_page=6)

    task_list = pagination.items

    return render_template("tasks.html",
                           tasks=task_list,
                           STATUS_LABELS=STATUS_LABELS,
                           Status=Status,
                           Priority=Priority,
                           PRIORITY_COLOURS=PRIORITY_COLOURS,
                           pagination=pagination,
                           search_term=search_term)


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
            priority=form.priority)

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


@tasks_bp.route("/update/<int:task_id>", methods=["GET", "POST"])
@login_required
def update(task_id: int):

    task = get_task_by_id(task_id)

    if request.method == "POST":

        form = UpdateTaskForm(request.form)

        if not form.success:
            for error in form.errors.values():
                flash(error, "error")
                return render_template("update-task.html",
                                       task=task,
                                       STATUS_LABELS=STATUS_LABELS,
                                       Status=Status,
                                       Priority=Priority)

        result = update_task(
            task_id=task_id,
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
                return render_template("update-task.html",
                                       task=task,
                                       STATUS_LABELS=STATUS_LABELS,
                                       Status=Status,
                                       Priority=Priority)

        flash("task successfully updated!", "success")
        return redirect(url_for("tasks.tasks"))

    return render_template("update-task.html",
                           task=task,
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


@tasks_bp.route("/complete/<int:task_id>", methods=["POST"])
@login_required
def complete(task_id:int):

    result = complete_task(task_id=task_id, user_id=current_user.id)
    if not result.success:
        for error in result.errors.values():
            flash(error, "error")
        return redirect(url_for("tasks.tasks"))

    flash("task completed!", "success")
    return redirect(url_for("tasks.tasks"))


@tasks_bp.route("/detail/<int:task_id>")
@login_required
def detail(task_id: int):

    task = get_task_by_id(task_id)

    if not task:
        flash("task does not exist!", "error")
        return redirect(url_for("tasks.tasks"))

    return render_template("detail.html",
                           task=task,
                           STATUS_LABELS=STATUS_LABELS,
                           PRIORITY_COLOURS=PRIORITY_COLOURS)
