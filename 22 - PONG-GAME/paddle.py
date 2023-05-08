from turtle import Turtle

# X_POS = 350
Y_POS = 0


class RightPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.X_POS = 350
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.goto(self.X_POS, Y_POS)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.X_POS, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.X_POS, new_y)


class LeftPaddle(RightPaddle):
    def __init__(self):
        super().__init__()
        self.X_POS = -350
        self.goto(self.X_POS, Y_POS)
