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
