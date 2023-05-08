from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def steer_left():
    tim.left(10)


def steer_right():
    tim.right(10)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=steer_left)
screen.onkey(key="d", fun=steer_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
