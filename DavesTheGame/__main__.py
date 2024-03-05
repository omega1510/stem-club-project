import os
import sys
import subprocess

sys.path.append(os.path.abspath(f"{os.getcwd()}/DavesTheGame/"))

import colorama

from choice import Choice
from situation import Situation

import story

class State:
    
    def __init__(self):
        self.game_won: bool = False
        self.game_over: bool = False

        self.current_situation = story.office

state = State()

def game_won():
    print(colorama.Back.GREEN + colorama.Fore.WHITE + "YOU WIN!" + colorama.Style.RESET_ALL)

def game_over():
    print(colorama.Back.RED + colorama.Fore.WHITE + "GAME OVER" + colorama.Style.RESET_ALL)

def clear():
    _ = subprocess.call('clear' if os.name == 'posix' else 'cls')

def game_loop():
    print(state.current_situation)

    while not state.game_won and not state.game_over:
        state.current_situation = Situation.advance(state.current_situation)
        clear()
        print(state.current_situation)
        state.game_won = state.current_situation.game_won
        state.game_over = state.current_situation.game_over

    if state.game_won:
        game_won()
    if state.game_over:
        game_over()

if __name__=="__main__":
    game_loop()
