import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]
# for i in range(3, 10):
#     tim.pencolor(random.choice(colors))
#     for sides in range(i):
#         angle = 360/i
#         tim.forward(100)
#         tim.right(angle)
tim.pensize(1)
tim.speed("fastest")

# for _ in range(100):
#     rotate = random.choice(directions)
#     tim.forward(30)
#     tim.setheading(rotate)
#     tim.pencolor(random_colour())

for c in range(0, 365, 5):
    tim.circle(100)
    tim.setheading(c)
    tim.color(random_colour())


screen = Screen()
screen.exitonclick()