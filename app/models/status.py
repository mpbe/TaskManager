from enum import Enum


class Status(str,Enum):
    TO_DO= "to_do"
    IN_PROGRESS="in_progress"
    COMPLETED="completed"