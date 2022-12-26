from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle_1(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.ORIGINAL_COORDINATES = [x_coordinate, y_coordinate]
        self.original_position = (self.ORIGINAL_COORDINATES[0], self.ORIGINAL_COORDINATES[1])
        self.goto(self.original_position)
        self.shape("square")
        self.color("white")
        self.left(90)
        self.penup()
        self.shapesize(1, 5)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.forward(-MOVE_DISTANCE)


