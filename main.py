from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Car
from random import randint
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Crossing Turtle")

player1 = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player1.move, key="w")

movement_increment = 0.5
time_sleep = 0.1
game_on = True
car_list = []

while game_on:
    chance = randint(1, 6)
    time.sleep(time_sleep)
    screen.update()
    if chance == 1:
        car = Car()
        car_list.append(car)
    for car in car_list:
        if player1.distance(car) <= 22:
            scoreboard.game_over()
            game_on = False

    if player1.is_at_finish_line():
        scoreboard.increase_level()
        time_sleep *= movement_increment

    for car in car_list:
        if car.xcor() > -350:
            car.move_car()

screen.exitonclick()
