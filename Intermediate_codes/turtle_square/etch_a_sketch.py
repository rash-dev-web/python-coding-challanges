from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

t.forward(50)


def move_forward():
    t.forward(20)


def move_backward():
    t.backward(20)


def move_left():
    t.left(20)


def move_right():
    t.right(20)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.listen()









screen.exitonclick()