from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.score=0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def get_score(self):
        self.score+=1
        self.update_score()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()


    """def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=("Arial", 24, "normal"))"""