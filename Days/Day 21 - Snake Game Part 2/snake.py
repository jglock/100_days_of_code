from turtle import Turtle

class Snake():
    
    def __init__(self):
        self.body_parts = []
        
        self.create_snake()


    def create_snake(self):
        for _ in range(3):
            self.add_segment((0 - 20 * _, 0))
        
        self.head = self.body_parts[0]

    def move(self):
        for body_part in range(len(self.body_parts)-1, 0, -1):
            self.body_parts[body_part].goto(self.body_parts[body_part-1].position())
        self.head.forward(20)
        
    def add_segment(self, position):
            self.body_parts.append(Turtle("square"))
            self.body_parts[-1].color("white")
            self.body_parts[-1].penup()
            self.body_parts[-1].goto(position)
    
    
    def reset(self):
        for seg in self.body_parts:
            seg.goto(1000,1000)
        self.body_parts.clear()
        self.create_snake()

    def extend(self):
        #add a new segmet to the snake
        self.add_segment(self.body_parts[-1].position())
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90) 
               
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)   
             
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)    
            
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def wallcollision(self):
        return self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280
    
    def tailcollision(self):
        
        for part in self.body_parts[1:]:
            if self.head.distance(part) < 10:
                return True
        return False