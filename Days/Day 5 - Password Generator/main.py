'''
Simple Password Generator using letters (lower and upper), numbers and symbols
'''

import string
from random import Random, sample

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input("How many symbols would you like?\n"))

nr_numbers = int(input("How many numbers would you like?\n"))


# Create a list of all pools used for the password 
# 🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗🠗
different_pools = ["letters"]

if nr_symbols > 0:
    different_pools.append("symbols")

if nr_numbers > 0:
    different_pools.append("numbers")
# 🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕🠕

# Define empty password string which will be concatenated in the upcoming for loop
password = ""


for letter in range(nr_letters - 1):

    # Choose one of the character-pools
    random_pool = sample(different_pools, k=1)[0]
    
    if random_pool == "symbols":
        
        # Symbols should only be added until the limit given by 'nr_symbols' is reached. Afterwards, the symbols-pool is removed from the the list of character pools.
        nr_symbols -= 1
        
        if nr_symbols == 0:
            different_pools.remove("symbols")
        
        password += sample(string.punctuation, k=1)[0]

    elif random_pool == "numbers":
        
        # Numbers should only be added until the limit given by 'nr_numbers' is reached. Afterwards, the numbers-pool is removed from the the list of character pools.
        nr_numbers -= 1

        if nr_numbers == 0:
            different_pools.remove("numbers")

        password += sample(string.digits, k=1)[0]
    
    else:

        password += sample(string.ascii_letters, k=1)[0]

print(f"Here is your password: {password}")