"""Implementation for situations in the game.

Implemented as a direted graph."""

# for fancy choice prompts
import survey

class Situation:
    """Situation Class

    A situation is a piece of text and associated choices. Each choice returns
    the next situation in the graph.

    Args:
        text: The text to display when a node is printed.
        game_won: Whether or not the game is won after this situation.
        game_over: Whether or not the game is lost after this situation.

    Methods:
        add_choice(): Add a new connection to the directed graph. Must be a
        `Choice` object. See DavesTheGame/choice.py.
        advance: Prompt the user for a choice and return the resulting situation.
    """

    def __init__(self, text: str, game_won: bool = False, game_over: bool = False):
        self.text = text
        self.choices = []
        self.game_won = game_won
        self.game_over = game_over

    def add_choice(self, choice):
        self.choices.append(choice)

    def __str__(self) -> str:
        return self.text

    @staticmethod
    def advance(situation):
        return situation.choices[survey.routines.select("What will you do: ", options = [str(choice) for choice in situation.choices])].result
