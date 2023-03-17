from turtle import Turtle

X = 10
Y = 10
INITIAL_SPEED = 0.1
class Ball(Turtle):
    """
    Class object to generate the game's ball, control its speed,
    starting location, and detect collisions with boundaries and player
    paddles.
    """

    def __init__(self):
        super().__init__()
        self.make_ball()
        self.move_x = X
        self.move_y = Y
        self.speed = INITIAL_SPEED
        self.starting_position()

    def make_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
    def starting_position(self):
        self.goto(0,0)
        self.speed = INITIAL_SPEED
        self.bounce_x()
    def bounce_x(self):
        self.move_x *= -1
        self.change_speed()
    def bounce_y(self):
        self.move_y *= -1
        self.change_speed()

    def move_ball(self):
        new_x = self.xcor()+self.move_x
        new_y = self.ycor()+self.move_y
        self.goto(new_x,new_y)
    def change_speed(self):
        if self.speed > 0: self.speed *= 0.9

