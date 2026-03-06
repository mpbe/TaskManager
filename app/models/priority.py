from enum import Enum


class Priority(str, Enum):
    LOW= "Low"
    MEDIUM= "Medium"
    HIGH= "High"


PRIORITY_COLOURS = {
    Priority.LOW: "text-green-700 bg-green-100",
    Priority.MEDIUM: "text-yellow-700 bg yellow-100",
    Priority.HIGH: "text-red-700 bg-red-100"
}