from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.file = open("data.txt")
        self.get_score = self.file.read()
        self.high_score = int(self.get_score)
        self.file.close()

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score = {self.total_score} High Score = {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.total_score = 0
        self.write_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over...", align=ALIGN, font=FONT)

    def update_score(self):
        self.total_score += 1
        # self.clear()
        self.write_score()
