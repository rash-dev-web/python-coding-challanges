from turtle import Turtle
MOVE = 20


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1, 1)
        self.penup()
        self.goto(location)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)
