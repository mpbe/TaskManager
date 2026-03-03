from enum import Enum


class Status(str,Enum):
    TO_DO= "to_do"
    IN_PROGRESS="in_progress"
    COMPLETED="completed"

STATUS_LABELS = {
    Status.TO_DO: "To Do",
    Status.IN_PROGRESS: "In Progress",
    Status.COMPLETED: "Completed"
}