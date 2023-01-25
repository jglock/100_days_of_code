"""
First part of the classic Snake Game. In this version, the snake is animated, moves and its direction can be entered through the arrow keys.
"""

from turtle import Screen
import time
from snake import Snake



game_active = True

screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title("Python Snake Game")

screen.tracer(0)


simon = Snake()

screen.update()



screen.listen()
screen.onkey(simon.up,"Up")
screen.onkey(simon.down,"Down")
screen.onkey(simon.left,"Left")
screen.onkey(simon.right,"Right")


while game_active:
    simon.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()