"""
the results classes for auth, inheriting from base. they return a user
object that will, on a validation failure be assigned the default of None, but
on a success will be assigned a User. this will be done in the service layer
"""

from dataclasses import dataclass
from app.models import User
from app.schema.base_result import BaseResult

@dataclass
class LoginResult(BaseResult):
   user: User | None = None


@dataclass
class RegisterResult(BaseResult):
   user: User | None = None
