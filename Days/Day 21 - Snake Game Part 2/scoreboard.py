from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt') as f:
            self.high_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()    
    
    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()