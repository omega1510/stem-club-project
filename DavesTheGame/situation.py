import survey

class Situation:

    def __init__(self, text: str, game_won=False, game_over=False):
        self.text = text
        self.choices = []
        self.game_won = game_won
        self.game_over = game_over

    def add_choice(self, choice):
        self.choices.append(choice)

    def __str__(self):
        return self.text

    @staticmethod
    def advance(situation):
        return situation.choices[survey.routines.select("What will you do: ", options = [str(choice) for choice in situation.choices])].result
