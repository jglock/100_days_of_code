'''
Simple Rock Paper Scissors game you play against the computer
'''
import ascii_art
from random import randint


while True:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

    if choice in "012":
        break
    print("Please choose either Rock, Paper or Scissors!")


print(ascii_art.ascii_dict[choice])

comp_choice = str(randint(0,2))

print("Computer chose:\n")

print(ascii_art.ascii_dict[comp_choice])

if choice == comp_choice:
    print("It's a draw!")
elif (choice == "0" and comp_choice == "2") or (choice == "1" and comp_choice == "0") or (choice == "2" and comp_choice == "1"):
    print("You win =)")
else:
    print("You lose =(")