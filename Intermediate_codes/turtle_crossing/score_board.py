from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level : {self.level}", align="center", font=("Courier", 20, "normal"))

    def point(self):
        self.level += 1
        self.update_scoreboard()
