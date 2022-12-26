###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random

import colorgram
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


color_list = [(245, 243, 238), (246, 242, 244), (240, 245, 241), (236, 239, 243), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (14, 98, 70),
              (232, 176, 165), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = Turtle()
tim.penup()
initial_y_coordinate = -200
tim.speed("fastest")
for i in range(10):
    tim.setpos(-300, initial_y_coordinate)
    initial_y_coordinate += 50
    for y in range(10):
        tim.dot(20, random_color())
        tim.fd(50)

tim.hideturtle()
screen.exitonclick()
