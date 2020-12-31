from turtle import Turtle
STARTING_POSITION = (-20, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # def move(self):
    #     self.forward(MOVE_DISTANCE)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_other_side(self):
        if self.ycor() == 280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
