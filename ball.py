from turtle import Turtle

X = 10
Y = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.make_ball()
        self.move_x = X
        self.move_y = Y
        self.starting_position()

    def make_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
    def starting_position(self):
        self.goto(0,0)
        self.bounce_x()
    def bounce_x(self):
        self.move_x *= -1
    def bounce_y(self):
        self.move_y *= -1

    def move_ball(self):
        new_x = self.xcor()+self.move_x
        new_y = self.ycor()+self.move_y
        self.goto(new_x,new_y)

