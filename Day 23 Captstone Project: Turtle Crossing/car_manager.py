from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1.0, stretch_len=2.0)
        random_color = random.choice(COLORS)
        self.color(random_color)
        random_x = random.randint(-300, 300)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
