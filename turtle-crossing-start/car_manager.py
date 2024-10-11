from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.cars = []


    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-250, 250))
            new_car.setheading(180)
            self.cars.append(new_car)


    def move_cars(self):
        for car in self.cars:
            car.forward(self.starting_move_distance)


    def speed_up(self):
        self.starting_move_distance += MOVE_INCREMENT
        self.move_cars()