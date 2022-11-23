from turtle import Turtle

FONT = ("Patrick Hand", 11, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.change_high_score()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def change_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def get_high_score(self):
        with open("high_score.txt") as file:
            content = int(file.read())
            return content
