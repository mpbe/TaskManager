from app.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash

"""
this is the user service, where i have some methods to perform simple CRUD operations
"""

def list_all_users():
    return [
            {"username": user.username,
             "email": user.email,
             "password hash": user.hashed_password
            }
            for user in User.query.all()]


def get_user_by_id(user_id: int):
    return User.query.get(user_id)


def delete_user(user_id: int):
    user = get_user_by_id(user_id)

    if not user:
        return False

    db.session.delete(user)
    db.session.commit()
    return True


def update_password(user_id: int, password: str):
    user = get_user_by_id(user_id)

    if not user:
        return False

    user.hashed_password = generate_password_hash(password)
    db.session.add(user)
    db.session.commit()
    return True