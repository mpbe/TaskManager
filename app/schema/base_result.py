"""
this is a class to take information from service validation. it works in a similar
fashion to the form class, but is a dataclass as it does not do the validation
itself. as it is a dataclass it uses the field attribute to ensure that
the errors dictionary is not shared between created objects but instead
created with each instance
"""

from dataclasses import dataclass, field


@dataclass
class BaseResult:
    errors: dict[str, str] = field(default_factory=dict)

    @property
    def success(self):
        return not self.errors

