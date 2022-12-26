from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t1 = Turtle(shape="turtle")
t1.penup()
t1.color(colors[0])
t1.goto(x=-230, y=-100)

t2 = Turtle(shape="turtle")
t2.penup()
t2.color(colors[1])
t2.goto(x=-230, y=-50)

t3 = Turtle(shape="turtle")
t3.penup()
t3.color(colors[2])
t3.goto(x=-230, y=0)

t4 = Turtle(shape="turtle")
t4.penup()
t4.color(colors[3])
t4.goto(x=-230, y=50)

t5 = Turtle(shape="turtle")
t5.penup()
t5.color(colors[4])
t5.goto(x=-230, y=100)

t6 = Turtle(shape="turtle")
t6.penup()
t6.color(colors[5])
t6.goto(x=-230, y=150)

all_turtles = [t1, t2, t3, t4, t5, t6]

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
