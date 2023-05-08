# import colorgram
#
# rgb_colors = []
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_to_list = r, g, b
#     rgb_colors.append(rgb_to_list)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
screen = Screen()
tim.speed("fastest")
tim.hideturtle()
color_list = [(243, 234, 76), (211, 158, 93), (188, 12, 69), (111, 179, 208), (25, 116, 169), (172, 172, 31), (221, 128, 166), (160, 78, 35), (128, 186, 146), (10, 32, 76), (235, 73, 41), (217, 67, 108), (31, 135, 83), (176, 48, 95), (234, 165, 194), (79, 13, 63), (12, 55, 34), (236, 228, 6), (29, 164, 207), (15, 42, 132), (58, 165, 95), (135, 213, 228), (9, 102, 63), (134, 36, 21), (93, 29, 12), (156, 211, 190)]
tim.penup()
x = -250
y = -250
tim.setposition(x, y)

for line in range(10):
    for dot in range(-250, 250, 50):
        tim.setposition(x, y)
        tim.dot(20, random.choice(color_list))
        x += 50
    y += 50
    x = -250


screen.exitonclick()