from app.schema.base_result import BaseResult
from dataclasses import dataclass
from app.models import Task


@dataclass
class CreateTaskResult(BaseResult):

    task: Task | None = None


class DeleteTaskResult(BaseResult):
    pass