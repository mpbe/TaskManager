from app.extensions import db
from app.models import User
from app.schema.auth_result import LoginResult, RegisterResult
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError

"""
service for auth, where more validation is performed and any queries/commits to the database
are made. service does not know about flask so keeping any routing/login logic out of here
"""

def authenticate_user(username: str, password: str):

    result = LoginResult()
    user = User.query.filter_by(username=username).first()

    if not user:
        result.errors["username"] = "user not in database"
        return result

    if not check_password_hash(user.hashed_password, password):
        result.errors["password"] = "password incorrect"
        return result

    result.user = user
    return result


def register_user(username: str, email: str, password: str):

    result = RegisterResult()

    if User.query.filter_by(username=username).first():
        result.errors["username"] = "user already exists in database"
        return result

    if User.query.filter_by(email=email).first():
        result.errors["email"] = "email already exists in database"
        return result

    if len(username) < 4:
        result.errors["username_length"] = "username cannot be less than 4 characters"

    if len(username) > 100:
        result.errors["username_length"] = "username cannot be longer than 100 characters"

    if len(email) > 100:
        result.errors["email_length"] = "email cannot be longer than 100 characters"

    if not is_valid_email(email=email):
        result.errors["email-format"] = "email is in incorrect format"

    if len(password) < 4:
        result.errors["password"] = "password cannot be shorter than 4 characters"

    if len(password) > 200:
        result.errors["password"] = "password cannot be longer than 200 characters"

    if not result.success:
        return result

    user = User(
        username=username,
        email = email,
        hashed_password = generate_password_hash(password=password)
    )

    db.session.add(user)
    db.session.commit()

    result.user = user
    return result


def is_valid_email(email: str):

    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False