from datetime import date
from app.extensions import db
from app.models import Status, Priority, Task
from app.schema.task_result import CreateTaskResult


def get_user_tasks(user_id: int):

    return Task.query.filter_by(user_id=user_id).all()


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