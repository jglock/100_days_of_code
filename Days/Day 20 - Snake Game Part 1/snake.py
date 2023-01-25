from turtle import Turtle

class Snake():
    
    def __init__(self):
        self.body_parts = []
        
        for _ in range(3):
            self.body_parts.append(Turtle("square"))
            self.body_parts[_].color("white")
            self.body_parts[_].penup()
            self.body_parts[_].setx(0 - 20 * _)


    def move(self):
        for body_part in range(len(self.body_parts)-1, 0, -1):
            self.body_parts[body_part].goto(self.body_parts[body_part-1].position())
        self.body_parts[0].forward(20)
        
    
    def up(self):
        if self.body_parts[0].heading() != 270:
            self.body_parts[0].setheading(90) 
               
    def down(self):
        if self.body_parts[0].heading() != 90:
            self.body_parts[0].setheading(270)   
             
    def right(self):
        if self.body_parts[0].heading() != 180:
            self.body_parts[0].setheading(0)    
            
    def left(self):
        if self.body_parts[0].heading() != 0:
            self.body_parts[0].setheading(180)