from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle()
player_2 = Paddle()
ball = Ball()
p1_score = Scoreboard()
p2_score = Scoreboard()

p1_score.p1_score()
p1_score.p2_score()

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
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 270:
        ball.direction()

screen.exitonclick()