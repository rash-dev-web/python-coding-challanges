from turtle import Turtle
from turtle import Screen
from Intermediate_codes.turtle_crossing.player import Player
from Intermediate_codes.turtle_crossing.car_manager import CarManager
from Intermediate_codes.turtle_crossing.score_board import ScoreBoard
import time

screen = Screen()
player = Player()

car_manager = CarManager()
score = ScoreBoard()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")

screen.listen()
screen.onkey(player.up, key="Up")


game_is_on = True
car_num = 0
score.point()
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_num += 1

    # create cars and move
    if car_num == 8:
        car_manager.generate_car()
        car_num = 0
    car_manager.move()

    # check collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    # detect a successful crossing
    if player.is_other_side():
        player.go_to_start()
        score.point()
        car_manager.speed_up()

screen.exitonclick()
