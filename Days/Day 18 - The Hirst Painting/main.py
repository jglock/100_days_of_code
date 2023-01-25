# import colorgram

# colors = colorgram.extract('image.jpg',30)

# rgb_values = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# print(rgb_values)

from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)

colors = [(202, 166, 109),  (153, 73, 47), (170, 152, 42), (222, 202, 137), (53, 93, 124), (136, 32, 22), (133, 163, 184), (48, 118, 87), (199, 92, 71), (16, 97, 75), (101, 73, 75), 
          (67, 47, 41), (147, 178, 148), (164, 142, 156), (234, 177, 165), (56, 46, 49), (130, 28, 32), (184, 205, 173), (41, 60, 72), (81, 146, 125), (184, 87, 92), (31, 78, 84), (48, 64, 81), (21, 69, 63), (219, 175, 178), (109, 124, 150)]

tim = Turtle()
tim.penup()
tim.hideturtle()

tim.setposition(tim.xcor() - 250, tim.ycor()-250)


for row in range(10):
    for column in range(10):
        tim.dot(20,color=choice(colors))
        tim.setx(tim.xcor() + 50)
    tim.sety(tim.ycor()+50)
    tim.setx(tim.xcor() - 500)



screen = Screen()

screen.exitonclick()