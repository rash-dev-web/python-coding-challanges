# import colorgram
#
# colors = colorgram.extract("hirst_painting_dot.jpg", 30)
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)

import turtle as t
from turtle import Screen
import random


color_list = [(194, 167, 126), (154, 144, 49), (142, 110, 35),
              (202, 200, 112), (94, 38, 21), (82, 111, 142), (84, 124, 121), (12, 38, 67), (89, 69, 77),
              (200, 144, 146), (178, 91, 89), (33, 85, 87), (34, 86, 82), (181, 91, 93),
              (93, 48, 38), (145, 167, 162), (144, 157, 171), (79, 41, 42), (105, 137, 134), (82, 49, 51),
              (214, 179, 176), (32, 69, 64), (209, 181, 184), (108, 127, 149), (178, 198, 194), (98, 138, 140)]


t.speed(0)
t.hideturtle()
t.colormode(255)
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)


for dot_num in range(1, 101):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if dot_num % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = t.Screen()
screen.exitonclick()
