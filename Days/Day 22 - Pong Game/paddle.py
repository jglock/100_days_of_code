from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle
        self.goto(coordinates)
        self.shapesize(stretch_wid=5, stretch_len=1)
    

    def up(self):
        self.sety(self.ycor()+20)

    def down(self):
        self.sety(self.ycor()-20)