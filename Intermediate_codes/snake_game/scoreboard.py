from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write_score()

    def write_score(self):
        self.write(f"Score = {self.total_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over...", align=ALIGN, font=FONT)

    def update_score(self):
        self.total_score += 1
        self.clear()
        self.write_score()
