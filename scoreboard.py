from turtle import Turtle

STYLE = ('Courier', 40, 'bold')
ALIGN = "center"
Y_COR = 240
P1_X = 80
P2_X = -80
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Generates scoreboard output
        """
        self.clear()
        self.goto(P1_X, Y_COR)
        self.write(f"{self.p1_score}",align=ALIGN,font=STYLE)
        self.goto(P2_X, Y_COR)
        self.write(f"{self.p2_score}", align=ALIGN, font=STYLE)
    def update_p1_score(self):
        """
        Add 1 to score and clear text in scoreboard title
        """
        self.p1_score += 1
        self.update_scoreboard()
    def update_p2_score(self):
        """
        Add 1 to score and clear text in scoreboard title
        """
        self.p2_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 15)
        self.write("GAME OVER", align=ALIGN, font=STYLE)







