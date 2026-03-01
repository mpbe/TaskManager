from app.extensions import db
from flask_login import UserMixin
from app.models.priority import Priority
from app.models.status import Status


class Task(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False, default=Status.TO_DO)
    priority = db.Column(db.Enum(Priority), nullable=False, default = Priority.LOW)