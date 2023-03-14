from turtle import Turtle, Screen

W = 20
H = 100
P1_X = 350
P2_X = -350
Y = 0

class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def make_player(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()

    def p1_start(self):
        self.make_player()
        self.goto(P1_X, Y)

    def p2_start(self):
        self.make_player()
        self.goto(P2_X, Y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)