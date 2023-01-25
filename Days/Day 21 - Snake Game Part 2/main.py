from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_active = True

screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title("Python Snake Game")

screen.tracer(0)


simon = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()



screen.listen()
screen.onkey(simon.up,"Up")
screen.onkey(simon.down,"Down")
screen.onkey(simon.left,"Left")
screen.onkey(simon.right,"Right")


while game_active:
    
    screen.update()
    time.sleep(0.1)
    simon.move()
    
    #Detection of collision with food.
    if simon.head.distance(food) < 15:
        food.refresh()
        simon.extend()
        scoreboard.add_point()
        
    #Detection of collision with wall or tail.
    if simon.wallcollision() or simon.tailcollision():
        game_active = False
        scoreboard.game_over()    
        
    
    
screen.exitonclick()