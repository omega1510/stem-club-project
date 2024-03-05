
class Choice:

    def __init__(self, text: str, result):
        self.text = text
        self.result = result

    def __str__(self):
        return self.text
