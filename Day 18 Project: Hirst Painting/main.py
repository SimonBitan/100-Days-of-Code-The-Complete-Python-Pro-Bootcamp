# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

colormode(255)
color_list = [(219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174), (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53), (232, 209, 16), (74, 79, 40), (44, 70, 45)]


def dot_maker():
    for _ in range(9):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.color(random.choice(color_list))
    tim.dot(20)


def turn_left():
    tim.left(90)
    tim.forward(50)
    tim.left(90)


def turn_right():
    tim.right(90)
    tim.forward(50)
    tim.right(90)

tim = Turtle()
tim.hideturtle()
tim.speed(0)
tim.penup()
tim.isvisible()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


# Each circle size 20, 50 space in between, make 10 x 10 grid
rows = 0
while rows < 10:
    dot_maker()
    rows += 1
    turn_left()
    dot_maker()
    turn_right()
    rows += 1


screen = Screen()
screen.exitonclick()
