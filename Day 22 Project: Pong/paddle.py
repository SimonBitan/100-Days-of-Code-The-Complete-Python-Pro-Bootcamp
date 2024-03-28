from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.turtlesize(stretch_wid=5.0, stretch_len=1.0)
        self.penup()
        self.shape("square")
        self.goto(position)

    # Functions to move the paddle.
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
