# Description

## Rules:
- Don't let the ball go pass your pad.
- For left player "w" moves the pad up and "s" key moves the pad down.
- For right player up key moves the pad up and down key moves the pad down.

https://user-images.githubusercontent.com/63066897/209573726-d85f3123-32f1-458c-aefd-afe1156975c4.mov


## Folder contents

In myCode folder it contains my own personal code for the ping-pong game.
</br>
mycode folder consist of the following files:
- ball.py
- main.py
- paddle_1.py
- scoreboard.py

In the solutionCode folder it contains the solution code provided by the course instructor Dr Angela Yu for the ping-pong game.
</br>
solutionCode folder consist of the following files:
- ball.py
- main.py
- paddle.py
- scoreboard.py

## Files Description:

For both main.py is the file that is run such that the ping pong game gets activated. This is the file that is responsible for the initial user-interface of what is seen on the screen. 

For both ball.py is the file that contains the class Ball(Turtle) that inherits properties of the Turtle class. It contains the follwing methods:
- move(self) to ensure that the ball is constandtly moving.
- bounce_y(self) to ensure that the ball bounces off the wall when it hits the top or bottom of the wall.
- bounce_x(self) to ensure that the ball bounces off the paddle when it hits the left or right paddle.
- revert(self)/reset_position(self) to ensure that the ball returns to its original starting position whenever a point is scored on either side. 

For the paddle_1.py and paddle.py files, these are the files that are responsible for the paddle functions in the program. They are responsible for setting up theuser-interface for the paddles as well as controlling the paddle functions through their methods. These methods consist of the following:
- up(self)/go_up(self). This method is responsible for making the paddle go up whenever the up key is pressed in the case of the right paddle and "w" key is pressed in the case of the left paddle.
- down(self)/go_down(self). This method is responsible for making the paddle go up whenever the down key is pressed in the case of the right paddle and "s" key is pressed in the case of the left paddle.


For both the scoreboard.py files. This file contains the Scoreboard(Turtle) class that inherits its properties from the Turtle class. This class is responsible for updating the scoreboard as well as assigning points to the left and right players. It has the following methods which are:
- updated_scoreboard(self). This method is responsible for updating the scoreboard to show the most updated score.
- l_point(self). This method is responsible for assigning the point to the left player in the event that the left player scores.
- r_point(self). This method is responsible for assigning the point to the right player in the event that the right player scores.


