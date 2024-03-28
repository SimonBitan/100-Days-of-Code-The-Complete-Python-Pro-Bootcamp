from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.r_paddle_score = 0
        self.l_paddle_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_paddle_score, False, ALIGNMENT, FONT)
        self.goto(100, 200)
        self.write(self.r_paddle_score, False, ALIGNMENT, FONT)

    def r_score_increase(self):
        self.r_paddle_score += 1
        self.update_scoreboard()

    def l_score_increase(self):
        self.l_paddle_score += 1
        self.update_scoreboard()

