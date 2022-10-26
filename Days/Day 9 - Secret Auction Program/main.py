"""
Building a secret auction program
"""

import art
from replit import clear

print(art.gavel)
print("Welcome to the secret auction program.")

bidders = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid    

    if input("Are there any other bidders? Type 'yes' or 'no'.").lower() == "no":
        break
    else:
        clear()

print(f"The winner is {max(bidders, key=bidders.get)}.")