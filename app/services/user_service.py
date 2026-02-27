from app.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash

from app.schema.auth_result import UpdatePasswordResult

"""
this is the user service, where i have some methods to perform simple CRUD operations
"""

#note: this method is for my use only, i would never put this in an actual application!
def list_all_users():
    return [
            {
             "id": user.id,
             "username": user.username,
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


def update_user_password(user_id: int, password: str):
    user = get_user_by_id(user_id)

    if not user:
        return UpdatePasswordResult(errors= {"error": "user does not exist"})

    if len(password) < 4:
        return UpdatePasswordResult(errors= {"error": "password cannot be shorter than 4 characters"})

    user.hashed_password = generate_password_hash(password)
    db.session.commit()
    return UpdatePasswordResult()
