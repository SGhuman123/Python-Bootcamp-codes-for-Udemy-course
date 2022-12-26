from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("lime")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.starting_score}", True, align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))

    def update(self):
        self.clear()
        self.starting_score += 1
        self.goto(0, 260)
        self.update_scoreboard()
