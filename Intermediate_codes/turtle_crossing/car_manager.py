from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def generate_car(self):
        car = Turtle("square")
        car.shapesize(1, 3, 1)
        car.penup()

        car.color(random.choice(COLORS))
        car.setheading(180)
        y_location = random.randint(-250, 250)
        car.goto(300, y_location)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT)


