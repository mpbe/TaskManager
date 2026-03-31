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
        title="Plan weekend trip",
        description="Research destinations, compare prices, and book accommodation for a short getaway.",
        due_date=date.today() + timedelta(days=7),
        status=Status.TO_DO,
        priority=Priority.MEDIUM,
        user_id=user1.id
    )

    task2 = Task(
        title="Finish project report",
        description="Complete the final draft of the quarterly report and send it to the manager for review.",
        due_date=date.today() + timedelta(days=3),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task3 = Task(
        title="Grocery shopping",
        description="Buy essentials: milk, eggs, bread, vegetables, and snacks for the week.",
        due_date=date.today() + timedelta(days=7),
        status=Status.COMPLETED,
        priority=Priority.LOW,
        user_id=user2.id
    )

    task4 = Task(
        title="Workout routine",
        description="Complete a 45-minute workout session focusing on cardio and strength training.",
        due_date=date.today() + timedelta(days=2),
        status=Status.IN_PROGRESS,
        priority=Priority.MEDIUM,
        user_id=user2.id
    )

    task5 = Task(
        title="Read a book",
        description="Read at least 3 chapters of the current book and take notes on key ideas.",
        due_date=date.today() + timedelta(days=6),
        status=Status.TO_DO,
        priority=Priority.LOW,
        user_id=user1.id
    )

    task6 = Task(
        title="Update portfolio website",
        description="Add recent projects, improve layout, and fix responsiveness issues on mobile devices.",
        due_date=date.today() + timedelta(days=4),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task7 = Task(
        title="Call family",
        description="Catch up with family members and check in on how everyone is doing.",
        due_date=date.today() + timedelta(days=5),
        status=Status.TO_DO,
        priority=Priority.LOW,
        user_id=user2.id
    )

    task8 = Task(
        title="Clean apartment",
        description="Vacuum, dust surfaces, clean kitchen, and organize cluttered areas.",
        due_date=date.today() + timedelta(days=1),
        status=Status.IN_PROGRESS,
        priority=Priority.MEDIUM,
        user_id=user2.id
    )

    task9 = Task(
        title="Prepare presentation slides",
        description="Create slides for the upcoming meeting, including visuals and key metrics.",
        due_date=date.today() + timedelta(days=2),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task10 = Task(
        title="Fix login bug",
        description="Investigate and resolve authentication issue affecting user sign-ins.",
        due_date=date.today() + timedelta(days=1),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task11 = Task(
        title="Email client feedback",
        description="Respond to client questions and provide updates on requested changes.",
        due_date=date.today() + timedelta(days=2),
        status=Status.COMPLETED,
        priority=Priority.MEDIUM,
        user_id=user1.id
    )

    task12 = Task(
        title="Backup database",
        description="Run a full backup and verify data integrity for the production database.",
        due_date=date.today() + timedelta(days=1),
        status=Status.TO_DO,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task13 = Task(
        title="Team meeting prep",
        description="Review agenda, gather updates, and prepare talking points for the weekly sync.",
        due_date=date.today() + timedelta(days=2),
        status=Status.IN_PROGRESS,
        priority=Priority.MEDIUM,
        user_id=user1.id
    )

    task14 = Task(
        title="Refactor API endpoints",
        description="Improve code structure, reduce duplication, and optimize response times.",
        due_date=date.today() + timedelta(days=5),
        status=Status.TO_DO,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task15 = Task(
        title="Write unit tests",
        description="Increase test coverage for critical modules and fix failing test cases.",
        due_date=date.today() + timedelta(days=4),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task16 = Task(
        title="Plan next sprint",
        description="Define goals, prioritize backlog items, and allocate tasks to the team.",
        due_date=date.today() + timedelta(days=6),
        status=Status.TO_DO,
        priority=Priority.MEDIUM,
        user_id=user1.id
    )

    task17 = Task(
        title="Review pull requests",
        description="Go through open PRs, leave feedback, and approve changes where appropriate.",
        due_date=date.today() + timedelta(days=1),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    # --- New tasks for user1 to reach 20 total ---

    task18 = Task(
        title="Optimize database queries",
        description="Analyze slow queries and add indexing to improve performance.",
        due_date=date.today() + timedelta(days=3),
        status=Status.IN_PROGRESS,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task19 = Task(
        title="Write documentation",
        description="Document API endpoints and usage examples for developers.",
        due_date=date.today() + timedelta(days=7),
        status=Status.TO_DO,
        priority=Priority.MEDIUM,
        user_id=user1.id
    )

    task20 = Task(
        title="Set up CI/CD pipeline",
        description="Configure automated testing and deployment workflow.",
        due_date=date.today() + timedelta(days=5),
        status=Status.TO_DO,
        priority=Priority.HIGH,
        user_id=user1.id
    )

    task21 = Task(
        title="Research new tech stack",
        description="Explore potential frameworks and tools for the next project.",
        due_date=date.today() + timedelta(days=8),
        status=Status.TO_DO,
        priority=Priority.LOW,
        user_id=user1.id
    )

    task22 = Task(
        title="Monitor application logs",
        description="Check logs for errors and unusual activity in production.",
        due_date=date.today() + timedelta(days=1),
        status=Status.COMPLETED,
        priority=Priority.MEDIUM,
        user_id=user1.id
    )

    db.session.add_all([task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15, task16, task17, task18, task19, task20, task21, task22])
    db.session.commit()

    print("Database seeded.")