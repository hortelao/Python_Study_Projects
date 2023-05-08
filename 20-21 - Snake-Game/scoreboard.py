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
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.clear()
        self.write(f"Score : {self.score_count}  |  High Score : {self.high_score}", align="center", font=('Courier', 16, 'bold'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=('Courier', 25, 'bold'))

    def reset(self):
        if self.score_count > int(self.high_score):
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.score_count}")
        self.score_count = -1
        self.add()
