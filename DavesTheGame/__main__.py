"""Dave's: The Game - Main Source File

A text-adventure game where you play as Br. Waqas, a PE teacher who is trying
to get Dave's hot chicken for the boys. You face enemies like student Mohammad
Abidi and school administrator Sr. Basahat.
"""

# for importing and clearing the screen
import os
import sys
import subprocess

# add directory of lib files to path
sys.path.append(os.path.abspath(f"{os.getcwd()}/DavesTheGame/"))

# for colored terminal output
import colorama

# game library files
from choice import Choice
from situation import Situation

# game story
import story

class State:
    """The state of the game"""
    
    def __init__(self):
        self.game_won: bool = False
        self.game_over: bool = False

        self.current_situation = story.office

state = State()

def game_won():
    """Display "YOU WIN!" text

    Function is run when the player wins the game"""
    
    print(colorama.Back.GREEN + colorama.Fore.WHITE + "YOU WIN!" + colorama.Style.RESET_ALL)

def game_over():
    """Display "GAME OVER" text

    Function is run when the player loses the game"""
    
    print(colorama.Back.RED + colorama.Fore.WHITE + "GAME OVER" + colorama.Style.RESET_ALL)

def clear():
    """Function to clear the screen"""
    _ = subprocess.call('clear' if os.name == 'posix' else 'cls')

def game_loop():
    """Game loop"""
   
    print(state.current_situation)

    # check if game is won or lost
    while not state.game_won and not state.game_over:

        # advance the game
        state.current_situation = Situation.advance(state.current_situation)
        
        clear()
        
        print(state.current_situation)
        
        # update state
        state.game_won = state.current_situation.game_won
        state.game_over = state.current_situation.game_over
    
    # print final message
    if state.game_won:
        game_won()
        
    if state.game_over:
        game_over()

if __name__=="__main__":
    game_loop()
