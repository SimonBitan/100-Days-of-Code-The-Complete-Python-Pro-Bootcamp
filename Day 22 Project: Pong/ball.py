from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def increase_speed(self):
        self.move_speed *= .9

    # Bounces the ball off a wall if it hits the wall.
    def bounce_y(self):
        self.y_move *= -1

# Bounces the ball off a paddle if it hits a paddle.
    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
