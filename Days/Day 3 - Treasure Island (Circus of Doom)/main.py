"""
Circus of Carnage (Haloween-themed) is a rather simple text-adventure game based on a few conditionals, loops and functions.
Not finished yet!
"""
import ascii_art


def game_over(you_alive: bool, geoffrey_alive: bool, laura_alive: bool):
    exit()

def hut_event():
    input("\nYou find a hut with a strange scarecrow in the front garden. You hear cries for help from the hut.")

    
    while True:
        scarecrow_check = input("What are you doing? (Examine) the scarecrow? Going into the (hut)? ").lower()

        if scarecrow_check == "examine":
            input("\nYou approach the scarecrow with caution.")
            input("You cannot believe what you're seeing ...")
            print(ascii_art.skull)
            input("Instead of a normal scarecrow, it is a half-decomposed skeleton!")
            print("")
            print("")
            print("Text-Adventure not finished yet, thank you!")
            break
        elif scarecrow_check == "hut":            
            print("")
            print("")
            print("Text-Adventure not finished yet, thank you!")
            break
        else:
            print("Please write only one of the given options!")

def circus_event():
    
    print("")
    print("")
    print("Text-Adventure not finished yet, thank you!")


input("Welcome to Circus of Carnage!\nThis is a Haloween-themed text-adventure.\nIn order to see each next step of your adventure you have to press 'enter'.\nSometimes, you will have to choose between different options which will alter your experience on each run.\nHave fun!\n")

input("Your name is David and you are on a roadtrip with your best friends Geoffrey and Laura.")

input("You're kind of sleepy and get slightly off the road.")


print(ascii_art.tree)

while True:
    first = input("Suddenly, there's a tree! What do you do? Apply the emergency brake (apply)? Steer car to the left (left)? Steer car to the right (right)?")

    
    if first.lower() == "right":
        print(ascii_art.forest)
        print("There are even more trees in front of you! You cannot do anything anymore and hit the trees at full speed.\nNobody survives...")
        game_over(False,False,False)
    elif first.lower() =="left":
        print(ascii_art.dozer)
        print("There is a bulldozer right in front of you! You cannot do anything anymore and hit the bulldozer at full speed.\nNobody survives...")    
        game_over(False,False,False)
    elif first.lower() == "apply":
        break
    else:
        print("Please write only one of the given options!")

input("\n... It's dark ... your whole body is aching.\nSlowly you become aware of your surroundings.")

input("The car has run into the tree and is completely unusable.")

input("Luckily you survived the impact with only a few bruises.")

input("There is no trace of Laura and Geoffrey.")

input("You squeeze out of the bent car. The only thing you have with you is your pocket knife.\n")

while True:
    crow_bar_check = input("In front of you, you see a bulldozer blocking the road. Would you like to examine it? (Yes) or (No): ").lower()
    if crow_bar_check == "yes":
        crowbar = True
        print("\nYou have found a rusty crowbar and take it with you.")
        break
    elif crow_bar_check == "no":
        crowbar = False
        break
    else:
        print("Please write only one of the given options!")

while True:
    pfad_check = input("\nYou see a trail to your left and to your right you see a circus sign with an arrow pointing to the forest. Where are you going? (right) or (left):").lower()

    if pfad_check == "left":
        hut_event()
        break
    elif pfad_check == "right":
        circus_event()
        break
    else:
        print("Please write only one of the given options!")