import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########


range_value = 3
angle = 360
while range_value != 10:
    for _ in range(range_value):
        tim.forward(200)
        tim.left(int(angle/range_value))
    range_value += 1
