from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? (Red, Green, Blue, Yellow, Orange, Purple). "
                                                "Pick one: ").lower()

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtle_list = []
x = -240
y = -125
for color in colors:
    turtle_color = color
    color = Turtle(shape="turtle")
    color.color(turtle_color)
    color.penup()
    color.goto(x, y)
    turtle_list.append(color)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
        turtle.forward(random.randint(0, 10))

if winner == user_bet:
    print(f"You've won! The {winner} turtle was the winner!")
else:
    print(f"You've lost! The {winner} turtle was the winner!")


screen.exitonclick()