import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


number_of_circles = int(input("How many circles do you wish to see?"))
original_angle = 0

for i in range(number_of_circles):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(original_angle)
    original_angle += (360 / number_of_circles)

screen = t.Screen()
screen.exitonclick()
