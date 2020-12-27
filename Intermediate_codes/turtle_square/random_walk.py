import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color= (r, g, b)
    return color


def random_walk(total_step):
    direction = [0, 90, 180, 270]
    for _ in range(total_step):
        heading = random.choice(direction)
        t.setheading(heading)
        t.color(random_colour())
        t.forward(10)


t.speed("fastest")
t.pensize(5)
print(random_colour())
random_walk(100)
