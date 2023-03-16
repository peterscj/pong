from turtle import Turtle

STYLE = ('Courier', 40, 'bold')
ALIGN = "center"
Y_COR = 240
P1_X = 40
P2_X = -40
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def make_scoreboard(self):
        self.color("white")
        self.hideturtle()
        self.penup()

    def p1_score(self):
        self.make_scoreboard()
        self.goto(P1_X, Y_COR)
        self.increase_score()
    def p2_score(self):
        self.make_scoreboard()
        self.goto(P2_X, Y_COR)
        self.increase_score()

    def increase_score(self):
        """
        Generates scoreboard output
        """
        self.write(f"{self.score}",align=ALIGN,font=STYLE)
    def update_score(self):
        """
        Add 1 to score and clear text in scoreboard title
        """
        self.score += 1
        self.clear()
        self.increase_score()

    def game_over(self):
        self.goto(0, 15)
        self.write("GAME OVER", align=ALIGN, font=STYLE)







