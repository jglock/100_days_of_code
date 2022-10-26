"""
simple calculator app
"""

import art

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


def calculate(number_1:str):
    operator = input("Pick an operation: ")

    number_2 = input("What's the next number?: ")

    operation = f"{number_1} {operator} {number_2}"

    result = operations[operator](float(number_1),float(number_2))

    print(f"{operation} = {result}")

    next_calc = input(f"Type 'y' to continue calculating with {result}, or tpye 'n' to start a new calculation (or 'q' to quit!): ")

    if next_calc == "y":
        calculate(str(result))
    elif next_calc == "n":
        number_1 = input("What's your first number?: ")

        print("Operations:")
        print("+")
        print("-")
        print("*")
        print("/")

        calculate(number_1)
    else:
        exit()



operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}



print(art.calc)

number_1 = input("What's your first number?: ")

print("Operations:")
print("+")
print("-")
print("*")
print("/")

calculate(number_1)