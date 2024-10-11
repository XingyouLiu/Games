import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    if player.ycor() >= 270:
        player.success()
        scoreboard.add_point()
        carmanager.speed_up()

    for car in carmanager.cars:
        if player.distance(car) <= 20:
            player.collide()
            game_is_on = False

screen.exitonclick()