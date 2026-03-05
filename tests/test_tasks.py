from datetime import date, timedelta
from app.models import Priority, Status

def test_create_task_success(client):

    client.post("/auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    response = client.post("/tasks/create", data={
        "title": "test",
        "description": "test",
        "due_date": (date.today() + timedelta(days=3)).isoformat(),
        "status": Status.TO_DO.value,
        "priority": Priority.LOW.value

    }, follow_redirects=True)

    assert b"task successfully created!" in response.data


def test_update_task_success(client):
    client.post("/auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    client.post("/tasks/create", data={
        "title": "test",
        "description": "test",
        "due_date": (date.today() + timedelta(days=3)).isoformat(),
        "status": Status.TO_DO.value,
        "priority": Priority.LOW.value
    })

    response = client.post("/tasks/update/1", data={
        "title": "test2",
        "description": "test2",
        "due_date": (date.today() + timedelta(days=5)).isoformat(),
        "status": Status.IN_PROGRESS.value,
        "priority": Priority.MEDIUM.value
    }, follow_redirects=True)

    assert b"task successfully updated!" in response.data


def test_delete_task_success(client):

    client.post("/auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    client.post("/tasks/create", data={
        "title": "test",
        "description": "test",
        "due_date": (date.today() + timedelta(days=3)).isoformat(),
        "status": Status.TO_DO.value,
        "priority": Priority.LOW.value
    })

    response = client.post("/tasks/delete/1", follow_redirects=True)

    assert b"successfully deleted" in response.data