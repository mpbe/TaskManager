from app import create_app
from app.extensions import db
from app.models.priority import Priority
from app.models.user import User
from app.models.task import Task
from datetime import date, timedelta
from app.models.status import Status
from werkzeug.security import generate_password_hash


"""
seed the database with some default users and tasks by typing the below in the terminal:

python seed.py

there are 2 users:

user1
username - aaaa
password - test

user2
username - bbbb
password - test
"""

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="aaaa", email="aaaa@aa.com", hashed_password=generate_password_hash("test"))
    user2 = User(username="bbbb", email="bbbb@bb.com", hashed_password=generate_password_hash("test"))

    db.session.add_all([user1, user2])
    db.session.commit()

    task1 = Task(
            title="First task",
            description="Example task",
            due_date=date.today() + timedelta(days=7),
            status=Status.TO_DO,
            priority=Priority.LOW,
            user_id=user1.id
        )

    task2 = Task(
            title="Second task",
            description="Another task",
            due_date=date.today() + timedelta(days=3),
            status=Status.IN_PROGRESS,
            priority=Priority.HIGH,
            user_id=user1.id
        )

    task3 = Task(
            title="First task",
            description="Example task",
            due_date=date.today() + timedelta(days=7),
            status=Status.TO_DO,
            priority=Priority.LOW,
            user_id=user2.id
        )

    task4 = Task(
            title="Second task",
            description="Another task",
            due_date=date.today() + timedelta(days=3),
            status=Status.IN_PROGRESS,
            priority=Priority.HIGH,
            user_id=user2.id
        )

    db.session.add_all([task1, task2, task3, task4])
    db.session.commit()

    print("Database seeded.")