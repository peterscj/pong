from turtle import Turtle

POS_X = 10
POS_Y = 10
NEG_X = -10
NEG_Y = -10
LEFT = 180
RIGHT = 0

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.make_ball()
        self.x = POS_X
        self.y = POS_Y
        self.direction = RIGHT

    def make_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
    def moving_right_hit_top(self):
        self.y = NEG_Y
        self.x = POS_X
    def moving_right_hit_bottom(self):
        self.y = POS_Y
        self.x = POS_X
    def moving_left_hit_bottom(self):
        self.y = POS_Y
        # self.x = NEG_X
    def moving_left_hit_top(self):
        self.y = NEG_Y
        self.x = NEG_X
    def move_left(self):
        self.setheading(LEFT)
        self.direction = LEFT
    def move_right(self):
        self.setheading(RIGHT)
        self.direction = RIGHT
    def move_ball(self):
        new_x = self.xcor()+self.x
        new_y = self.ycor()+self.y
        self.goto(new_x,new_y)

