from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1


    def move(self):
        self.setx(int(self.xcor() + self.xmove))
        self.sety(int(self.ycor() + self.ymove))

    def wallcollision(self):
        return self.ycor() > 280 or self.ycor() < -280

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.movespeed *= 0.9

    def paddlecollision(self,paddle, border):
        if border > 0:
            return self.distance(paddle) < 50 and self.xcor() > border
        return self.distance(paddle) < 50 and self.xcor() < border

    def reset_position(self):
        self.bounce_x()
        self.goto(0,0)
        self.movespeed = 0.1