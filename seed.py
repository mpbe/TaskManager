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
            description="Lorem ipsum dolor sit amet consectetur adipiscing",
            due_date=date.today() + timedelta(days=7),
            status=Status.TO_DO,
            priority=Priority.LOW,
            user_id=user1.id
        )

    task2 = Task(
            title="Second task",
            description="Lorem ipsum dolor sit amet consectetur adipiscing elit quisque faucibus ex sapien vitae pellentesque sem placerat in id cursus mi.",
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

    task5 = Task(
        title="Third task",
        description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text",
        due_date=date.today() + timedelta(days=7),
        status=Status.TO_DO,
        priority=Priority.LOW,
        user_id=user1.id
    )

    task6 = Task(
        title="Fourth task",
        description="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' ",
        due_date=date.today() + timedelta(days=3),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task7 = Task(
        title="Third task",
        description="Example task",
        due_date=date.today() + timedelta(days=7),
        status=Status.TO_DO,
        priority=Priority.LOW,
        user_id=user2.id
    )

    task8 = Task(
        title="Fourth task",
        description="Another task",
        due_date=date.today() + timedelta(days=3),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user2.id
    )

    db.session.add_all([task1, task2, task3, task4, task5, task6, task7, task8])
    db.session.commit()

    print("Database seeded.")