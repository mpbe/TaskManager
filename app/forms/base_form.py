
"""
allegedly this is one of the things that WTForms automates but i wanted to try
and create these objects myself to get an idea how it works before i start
using WTForms in other projects

essentially these objects take in the information from the form and perform
simple validation such as if the field is empty.

this is a base form that the others can inherit from

"""

class BaseForm:

    def __init__(self):
        self.errors = {}

    @property
    def success(self):
        return not self.errors