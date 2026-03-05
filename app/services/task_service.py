from datetime import date
from app.extensions import db
from app.models import Status, Priority, Task
from app.schema.task_result import CreateTaskResult, DeleteTaskResult, UpdateTaskResult


def get_user_tasks(user_id: int):

    return Task.query.filter_by(user_id=user_id).all()


def get_task_by_id(task_id: int):
    task = Task.query.get(task_id)

    if not task:
        return "task does not exist"
    return task


def create_task(user_id: int, title: str, description: str, due_date: date, status: Status, priority: Priority):

    result = CreateTaskResult()
    if len(title) > 100 or len(title) < 4:
        result.errors["title_length"] = "title must be between 4 and 100 characters"

    if len(description) > 500:
        result.errors["description"] = "description cannot be longer than 500 characters"

    if due_date < date.today():
        result.errors["due_date"] = "due date cannot be in past"

    if not result.success:
        return result

    task = Task(
        user_id= user_id,
        title= title,
        description= description,
        due_date= due_date,
        status= status,
        priority= priority
    )

    db.session.add(task)
    db.session.commit()

    return CreateTaskResult(task=task)


def update_task(
        task_id: int, user_id: int, title: str, description: str,
        due_date: date, status: Status, priority: Priority):

    task = Task.query.get(task_id)
    result = UpdateTaskResult()


    if not task:
        result.errors["task"] = "task not in database"
        return result

    if task.user_id != user_id:
        result.errors["user"] = "unauthorised"
        return result


    if len(title) > 100:
        result.errors["title"] = "title cannot be longer than 100 characters"

    if len(description) > 500:
        result.errors["description"] = "description cannot be longer than 500 characters"

    if due_date < date.today():
        result.errors["time"] = "due date a cannot be in the past"

    if not result.success:
        return result


    task.title = title
    task.description = description
    task.due_date = due_date
    task.status = status
    task.priority = priority

    db.session.commit()

    return UpdateTaskResult(task=task)


def delete_task(task_id: int, user_id: int):

    task = Task.query.get(task_id)

    if not task:
        return DeleteTaskResult(errors= {"task is not in database": "error"})

    if task.user_id != user_id:
        return DeleteTaskResult(errors={"task": "unauthorised"})

    db.session.delete(task)
    db.session.commit()
    return DeleteTaskResult()
