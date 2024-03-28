from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-290, 260)
        self.level = 1
        self.write(f"Level: {self.level}", False, ALIGNMENT, FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", False, "center", FONT)
