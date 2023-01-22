"""
Higher Lower Game: two randomly selected facebook accounts from a list of dictionaries are presented and the player has to choose which of both accounts might've more followers.
If you're correct, you get a point and keep playing, if you lose, the final score is shown and the game is over.
"""


import random
from game_data import data
from art import logo,vs
import os

def cls():
    
    """
    Clears interpreter console.
    """
    os.system('cls' if os.name=='nt' else 'clear')

score = 0

while True:
    person1 = random.choice(data)
    person2 = random.choice(data)
    if person1 == person2:
        continue
    print(logo)
    print("Score:", score)
    print("Which person has more followers:")
    print("Compare 1:", person1['name'], "Description:", person1['description'], "Country:", person1['country'])
    
    print(vs)
    
    print("Against 2:", person2['name'], "Description:", person2['description'], "Country:", person2['country'])
    choice = input("Who has more followers? (1 or 2): ")
    cls()
    if int(choice) == 1 and person1['follower_count'] > person2['follower_count']:
        score += 1
    elif int(choice) == 2 and person2['follower_count'] > person1['follower_count']:
        score += 1
    else:
        print(logo)
        print("Incorrect. Game over. Final score:", score)
        break