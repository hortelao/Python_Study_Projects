import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

correct_count = 0

found = []
while correct_count < 50:
    user_answer = turtle.textinput(f"{correct_count}/50 States Correct", "What's the state's name?").title()
    if user_answer == "Exit":
        break
    if len(data[data.state == user_answer]) > 0 and user_answer not in found:
        found.append(user_answer)
        correct_count += 1

        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        data_main = data[data.state == user_answer]
        state.goto(int(data_main["x"]), int(data_main["y"]))
        state.write(user_answer)
