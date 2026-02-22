from app import User
from app.schema.auth_result import LoginResult
from werkzeug.security import generate_password_hash, check_password_hash


def authenticate_user(username: str, password: str):

    result = LoginResult
    result.user = User.query.filter_by(username=username).first()

    if not result.user:
        result.errors["user"] = "user not in database "

    if not check_password_hash(result.user.hashed_password, password):
        result.errors["password"] = "password incorrect"

    return result





    #register - uniqueness