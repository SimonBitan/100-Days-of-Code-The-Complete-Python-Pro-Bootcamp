from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.write("Score: 0", False, ALIGNMENT, FONT)

    def score_update(self, score):
        self.clear()
        self.write(f"Score: {score} ", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", False, ALIGNMENT, FONT)


