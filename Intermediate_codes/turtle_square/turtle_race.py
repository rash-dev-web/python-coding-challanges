from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_guess = screen.textinput("Make a bet...", "Place your bet on the turtle. Enter a color:")
colors = ["red", "blue", "green", "black", "yellow", "purple"]
is_race_on = False
x = -230
y_index = [-100, -60, -20, 20, 60, 100]

if user_guess:
    is_race_on = True


turtle_list = []
for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=x, y= y_index[turtle_index])
    turtle_list.append(new_turtle)

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_guess:
                print(f"You've won. {winning_turtle} has won the race!")
            else:
                print(f"You've lost. {winning_turtle} has won the race!")
        distance = random.randint(1, 10)
        turtle.forward(distance)


screen.exitonclick()