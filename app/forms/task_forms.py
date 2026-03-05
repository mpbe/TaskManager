from app.forms.base_form import BaseForm
from app.models.priority import Priority
from app.models.status import Status
from app.utils.parse_date import parse_date


class CreateTaskForm(BaseForm):

    def __init__(self, form):
        super().__init__()

        self.title = form.get("title", "").strip()
        if not self.title:
            self.errors["title"] = "title cannot be blank"

        self.description = form.get("description", "").strip()

        try:
            self.due_date = parse_date(form.get("due_date"))
        except ValueError:
            self.errors["date"] = "date format is incorrect"

        try:
            self.status = Status(form.get("status"))
        except ValueError:
            self.errors["status_type"] = "please select a status"

        if not self.status:
            self.errors["status"] = "status cannot be blank"

        try:
            self.priority = Priority(form.get("priority"))
        except ValueError:
            self.errors["priority_type"] = "please select a priority level"

        if not self.priority:
            self.errors["priority"] = "priority cannot be blank"


class UpdateTaskForm(BaseForm):

    def __init__(self, form):
        super().__init__()

        self.title = form.get("title", "").strip()
        if not self.title:
            self.errors["title"] = "title cannot be blank"

        self.description = form.get("description", "").strip()

        try:
            self.due_date = parse_date(form.get("due_date"))
        except ValueError:
            self.errors["due_date"] = "date in incorrect format"

        status_temp = form.get("status")

        if not status_temp:
            self.errors["status_blank"] = "status cannot be blank"

        try:
            self.status = Status(status_temp)
        except ValueError:
            self.errors["status"] = "please select a status"

        priority_temp = form.get("priority")

        if not priority_temp:
            self.errors["priority_blank"] = "priority cannot be blank"

        try:
            self.priority = Priority(priority_temp)
        except ValueError:
            self.errors["priority"] = "please select a priority level"
