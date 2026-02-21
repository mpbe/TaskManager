
"""
these are the forms for the auth route/service
"""
from app.forms.base_form import BaseForm


class LoginUserForm(BaseForm):

    def __init__(self, form):
        super().__init__()

        #if fails either validation errors will be truthy, and thus fail the success
        #method inherited from the base form. it is designed to flash all errors on
        #a fail rather than just the first

        self.username = form.get("username", "").strip()
        if not self.username:
            self.errors["username"] = "username must not be blank"

        self.password = form.get("password", "").strip()
        if not self.password:
            self.errors["password"] = "password must not be blank"


class RegisterUserForm(BaseForm):
    def __init__(self, form):
        super().__init__()

        self.username = form.get("username", "").strip()
        if not self.username:
            self.errors["username"] = "username must not be blank"

        self.email = form.get("email", "").strip()
        if not self.email:
            self.errors["email"] = "email must not be blank"

        self.password = form.get("password", "").strip()
        if not self.password:
            self.errors["password"] = "password must not be blank"






