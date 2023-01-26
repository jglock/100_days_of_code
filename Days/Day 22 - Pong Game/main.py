"""
Building the classic Pong Game using the turtle package.
"""


from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_active=True

screen = Screen()
screen.title("Python Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height = 600)
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()


screen.listen()


screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")


while game_active:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.wallcollision():
        ball.bounce_y()

    if ball.paddlecollision(right_paddle, 320) or ball.paddlecollision(left_paddle, -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()