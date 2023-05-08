from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-50, 235)
        self.write(self.l_score, align="center", font=("Courier", 45, "bold"))
        self.goto(50, 235)
        self.write(self.r_score, align="center", font=("Courier", 45, "bold"))

    def r_add(self):
        self.r_score += 1
        self.update()

    def l_add(self):
        self.l_score += 1
        self.update()