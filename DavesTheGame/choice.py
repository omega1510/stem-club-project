"""Implementation for a Choice
"""

class Choice:
    """Choice Class

    Choices connect situations to each other in a directed graph.

    Args:
        text: The text to display with the choice.
        result: The situation it leads to.
    """

    def __init__(self, text: str, result):
        self.text = text
        self.result = result

    def __str__(self):
        return self.text
