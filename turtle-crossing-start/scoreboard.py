from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(280,280)
        self.write(self.score, align="center", font=("Arial", 16, "normal"))

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

