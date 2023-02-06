import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.bgpic('blank_states_img.gif')
game_score = 0

states = pandas.read_csv("50_states.csv")
state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()
solutions = []

while game_score < 50:
    answer_state = screen.textinput(title=f"{game_score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states["state"].to_list() and answer_state not in solutions:
        game_score += 1
        row = states[states["state"] == answer_state]
        x = int(row.x)
        y = int(row.y)
        state_turtle.goto(x,y)
        state_turtle.write(answer_state)
        solutions.append(answer_state)



missed_states = states.query("state not in @solutions").state
missed_states.to_csv("states_to_learn.csv")