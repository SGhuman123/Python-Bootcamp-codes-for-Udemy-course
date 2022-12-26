from turtle import Screen
from snake import Snake, create_borders
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
create_borders()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update()

    # Detect collision with wall.
    if snake.head.xcor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        # if segment.pos() == snake.head.pos():
        #     continue
        if snake.head.distance(segment) < 1:
            game_is_on = False
            scoreboard.game_over()
            print(f"This is the first {snake.head.pos()}")

    # if head collides with any segment in the tail:

screen.exitonclick()
