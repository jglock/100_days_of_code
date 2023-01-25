"""
This script shows how a coffee machine should work based on the requirements stated in the PDF file and by using classes defined in the files "coffee_maker.py", "menu.py"  and "money_machine.py".
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
coffeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()



while True:
    user_input = input(f"What would you like? ({menu.get_items()}):")
    if menu.find_drink(user_input.lower()) in menu.menu:
        current_coffee = menu.find_drink(user_input.lower())
        if coffeMachine.is_resource_sufficient(current_coffee):
    
            if moneyMachine.make_payment(current_coffee.cost):

                coffeMachine.make_coffee(current_coffee)

    elif user_input.lower() == "off":
        print("Turning off the Coffee Machine...")
        break
    elif user_input.lower() == "report":
        coffeMachine.report()
        moneyMachine.report()
    else:
        print(f"Invalid selection. Please choose from {menu.get_items()}.")
