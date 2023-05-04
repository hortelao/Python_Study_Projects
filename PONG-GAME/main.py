from turtle import Screen
from paddle import RightPaddle, LeftPaddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right = RightPaddle()
left = LeftPaddle()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(right.move_up, "Up")
screen.onkeypress(right.move_down, "Down")

screen.onkeypress(left.move_up, "w")
screen.onkeypress(left.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        score.l_add()
    if ball.xcor() < -400:
        ball.reset()
        score.r_add()


screen.exitonclick()