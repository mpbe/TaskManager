from datetime import date, timedelta
from app.models import Priority, Status

def test_create_task_success(client):

    client.post("/auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    response = client.post("/tasks/create", data={
        "user_id": 100,
        "title": "test",
        "description": "test",
        "due_date": (date.today() + timedelta(days=3)).isoformat(),
        "status": Status.TO_DO.value,
        "priority": Priority.LOW.value

    }, follow_redirects=True)

    assert b"task successfully created!" in response.data