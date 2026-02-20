
"""
allegedly this is one of the things that WTForms automates but i wanted to try
and create these objects myself to get an idea how it works before i start
using WTForms in other projects

essentially these objects take in the information from the form and perform
simple validation such as if the field is empty.

this is a base form that the others can inherit from

i am aware that this does not need field etc as it is not a dataclass, but i wanted
it to conform to same style as my results objects i will create later
"""

from dataclasses import field


class BaseForm():

    def __init__(self):
        #ensures a new dict is created for each form object that is created
        self.errors: dict[str, str] = field(default_factory=dict)

    @property
    def success(self):
        return not self.errors
