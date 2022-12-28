"""
Simple Blackjack application
"""
    
from art import ascii_bj
from random import sample
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
active_game = True
player= []
computer= []

print(ascii_bj)


print("\n")


def draw_card(deck:list):
    new_card = sample(cards,1)[0]
    if new_card == 11 and sum(deck) + new_card > 21:
        deck.append(1)
    else:
        deck.append(new_card)
    
    
def check_blackjack(deck:list):
    if sum(deck) == 21:
        return True
    return False

def initilize_deck(deck:list):
    draw_card(deck)
    draw_card(deck)

def print_hands(show_computer:bool):
    if show_computer:
        print(f"Computer: {computer} => {sum(computer)}")
        print(f"Player:   {player} => {sum(player)}\n")
    else:        
        print(f"Computer: [{computer[0]},*] => ?")
        print(f"Player:   {player} => {sum(player)}\n")
    
def restart_game():
    if input("Do you want to start a new game? Yes (y) or No (n): ") == "y":
        global player
        global computer
        
        player = []
        computer = []
        initilize_deck(player)
        initilize_deck(computer)
        os.system('cls')
        print(ascii_bj)


        print("\n")
    else:
        global active_game
        
        active_game = False   
        
        
        
initilize_deck(player)
initilize_deck(computer)    


while active_game:
    if check_blackjack(computer):
        
        print_hands(True)
        print("Computer got Blackjack! You lost.")
        restart_game()
        
    elif check_blackjack(player):
        
        print_hands(True)
        print("You've got Blackjack! Well done, you win!!")        
        restart_game()
        
    elif sum(player) > 21:
        
        
        print_hands(True)
        print("You've lost, your score goes over 21.")
        restart_game()
        
    else:
        print_hands(False)

        if input("Do you want to get another card? Yes (y) or No (n): ") == "y":
            draw_card(player)
        else:
            while sum(computer) < 16:
                draw_card(computer)
            print_hands(True)
            
            if sum(computer) > sum(player):
                print("The Computer got a higher score than you. You lost!")
            elif sum(computer) == sum(player):
                print("You and the Computer got the same score. It's a Draw!")
            else:
                print("You got a higher score than the Computer. Congrats, you've won!")
            restart_game()
           