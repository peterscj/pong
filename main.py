from turtle import Turtle, Screen
import time
from paddle import Paddle
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle()
player_2 = Paddle()
player_1.p1_start()
player_2.p2_start()
screen.listen()

# Key Bindings
screen.onkey(player_1.up, "Up")
screen.onkey(player_1.down, "Down")
screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()