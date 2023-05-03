from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = -1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.add()

    def add(self):
        self.score_count += 1
        self.clear()
        self.write(f"Score = {self.score_count}", align="center", font=('Courier', 16, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Courier', 25, 'bold'))