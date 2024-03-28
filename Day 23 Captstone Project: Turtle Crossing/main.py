import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

NUMBER_OF_CARS = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initiate the player, scoreboard, and cars.
player = Player()
scoreboard = Scoreboard()

cars = []
for _ in range(NUMBER_OF_CARS):
    car = CarManager()
    cars.append(car)


# Move the player on button press.
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Move the cars.
    for car in cars:
        car.move()
        # Have the cars that crossed the screen go back to a random spot on before the right side border.
        if car.xcor() < -300:
            random_x = random.randint(301, 400)
            random_y = random.randint(-260, 260)
            car.teleport(random_x, random_y)
        # Detect if player gets hit by a car.
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    # Detect when player hits finish line and reset player position + increase speed of the cars.
    if player.ycor() == 280:
        player.reset_position()
        scoreboard.update_level()
        for car in cars:
            car.increase_speed()

screen.exitonclick()

