"""
    Simple Guessing Game in order to learn how to use variables with different scopes.
"""
import os
from random import randint
from art import logo


GAME_ACTIVE = True

def cls():
    
    """
    Clears interpreter console.
    """
    os.system('cls' if os.name=='nt' else 'clear')
    
def restart_game():
    
    """
    Player chooses whether he wants to start another round of Guessing Game.
    """
    
    global GAME_ACTIVE
    
    if input("Do you want to start a new game? Yes (y) or No (n): ") == "y":
        cls()
        
    else:
        GAME_ACTIVE = False
        

def start_game(MAX_LOOPS):
    
    """
    Starts a round of Guessing Game
    """
    
    global RANDOM_NUMBER
    
    for loop in range(1, MAX_LOOPS):
        
        print(f"You have {MAX_LOOPS - loop} attempts remaining to guess the number.")
        number = int(input("Guess a number: "))
        
        if number ==  RANDOM_NUMBER:
            print("Congrats, you've won!")
            
            restart_game()
            break
        
        if number > RANDOM_NUMBER:
            print(f"{number} is too high.")
        elif number < RANDOM_NUMBER:
            print(f"{number} is too low.")
        
        if loop == MAX_LOOPS - 1 and number != RANDOM_NUMBER:
            print("You've run out of guesses, you lose.")
        
            restart_game()
            break
        
        
        
while GAME_ACTIVE:

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    RANDOM_NUMBER = randint(1,100)
    
    if difficulty == 'easy':
        MAX_LOOPS = 10 + 1
        start_game(10 + 1)
    else:
        start_game(5 + 1)

        

    

