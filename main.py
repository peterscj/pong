from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

"""
Using the turtle library, code will execute the classic pong video game where
two players attempt to move a paddle to keep a ball bouncing between them until
one player successfully knocks the ball past the other player.

The various instruments of the game, including the scoreboard, paddles, and ball
are stored as class objects, and so the script is fully object oriented. All classes
are initialized to inherit properites of the Turtle class from the turtle library.
"""


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle()
player_2 = Paddle()
ball = Ball()
scoreboard = Scoreboard()

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
    time.sleep(ball.speed)
    screen.update()
    ball.move_ball()

    # Detect collision on top wall
    if abs(ball.ycor()) > 270:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(player_1) < 30 or ball.distance(player_2) < 30:
        ball.bounce_x()

    # Detect if ball passes paddle
    if ball.xcor() > 350:
        ball.starting_position()
        scoreboard.update_p1_score()

    # Detect if ball passses paddle
    if ball.xcor() < -350:
        ball.starting_position()
        scoreboard.update_p2_score()

screen.exitonclick()