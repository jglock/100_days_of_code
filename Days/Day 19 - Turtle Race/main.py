from turtle import Turtle, Screen
from random import randint


race_active = False

screen= Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for turtle_index in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[turtle_index].color(colors[turtle_index])
    turtles[turtle_index].penup()
    turtles[turtle_index].goto(x=-230, y=-50 + 20 * turtle_index)

if user_choice:
    race_active = True
    
    
while race_active:
    for turtle in turtles:
        random_distance = randint(0,10)
        turtle.forward(random_distance)

    if turtle.xcor() >= 230:
        race_active = False
        winner = turtle.pencolor()
        
        if winner == user_choice:
            print(f"You've won! The {winner} turtle is the winner!")
        else:
            print(f"You've lost! The {winner} turtle is the winner!")
