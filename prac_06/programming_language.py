"""
Programming Language class activity.
CP1404
Sophie Thomas.
"""


class ProgrammingLanguage:
    """something"""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.is_dynamic(), self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
