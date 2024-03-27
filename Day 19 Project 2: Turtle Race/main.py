from turtle import Turtle, Screen
import random

# Setup screen for desired size
screen = Screen()
screen.setup(width=500, height=400)

# Create turtles and move them to starting position.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
y_coords = [-100, -66, -33, 0, 33, 66, 100]
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_coords[turtle_index])

# Prompt user for a bet on which turtle will win.
bet = screen.textinput("Make a bet!", "Which color turtle will you bet on?: ")

# Have the turtles race until one reaches the edge of the screen.
race_active = True
while race_active:
    for turtle in turtles:
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            race_active = False
            if bet == turtle.pencolor():
                print("You won the bet!")
            else:
                print("You lost the bet.")
            print(f"The {turtle.pencolor()} turtle won.")

screen.exitonclick()
