"""
This script shows how a coffe machine should work based on the requirements stated in the PDF file.
"""
coffee_requirements = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "price": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "price": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "price": 3.0},
}

water = 2000
milk = 1000
coffee = 500
money = 0

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input.lower() in coffee_requirements:
        current_coffee = coffee_requirements[user_input.lower()]
        if water < current_coffee["water"]:
            print("Not enough water.")
        elif milk < current_coffee["milk"]:
            print("Not enough milk.")
        elif coffee < current_coffee["coffee"]:
            print("Not enough coffee.")
        else:
            print("Insert coins: (quarters, dimes, nickels, pennies)")
            quarters = int(input("Quarters: "))
            dimes = int(input("Dimes: "))
            nickels = int(input("Nickels: "))
            pennies = int(input("Pennies: "))
            inserted_money = round((quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01), 2)
            if inserted_money < current_coffee["price"]:
                print(f"Sorry, that's not enough money. Money refunded. {inserted_money}$")
            else:
                # code to dispense coffee
                water -= current_coffee["water"]
                milk -= current_coffee["milk"]
                coffee -= current_coffee["coffee"]
                money += current_coffee["price"]
                change = round(inserted_money - current_coffee["price"], 2)
                if change != 0:
                    print(f"Here is {change}$ in change.")
                print(f"Here is your {user_input}. Enjoy!")
    elif user_input.lower() == "off":
        print("Turning off the Coffee Machine...")
        break
    elif user_input.lower() == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    else:
        print("Invalid selection. Please choose from espresso, latte, or cappuccino.")
