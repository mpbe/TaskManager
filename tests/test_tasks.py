from datetime import date, timedelta
from app.models import Priority, Status


def test_create_task_success(client):

    client.post("/tasks/create", data={
        "user_id": 100,
        "title": "test",
        "description": "test",
        "due_date": date.today() + timedelta(days=3),
        "status": Status.TO_DO,
        "priority": Priority.LOW

    }, follow_redirects=True)

    assert b"task successfully created!"