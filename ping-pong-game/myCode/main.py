from turtle import Screen
from paddle_1 import Paddle_1
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

paddle_r = Paddle_1(350, 0)
paddle_l = Paddle_1(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

game_is_on = True
sleep_time = 0.05

while game_is_on:
    if sleep_time < 0:
        sleep_time = 0.01

    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        sleep_time -= 0.01

    # Detect R paddle misses
    if ball.xcor() > 360:
        ball.revert()
        scoreboard.l_point()
        paddle_r.setpos(350, 0)
        paddle_l.setpos(-350, 0)
        sleep_time = 0.05

    # Detect L paddle misses
    if ball.xcor() < -360:
        ball.revert()
        scoreboard.r_point()
        paddle_r.setpos(350, 0)
        paddle_l.setpos(-350, 0)
        sleep_time = 0.05

screen.exitonclick()
