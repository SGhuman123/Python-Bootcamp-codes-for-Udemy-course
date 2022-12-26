# Description

## How the game works:

In this game, I create a turtle crossing game where the turtle is not allowed to hit the cars as it attempts to reach the end of the road. Once it reaches the end of the road, the turtle would then progress on to the next level where cars now move at faster speeds that make it harder for the turtle to reach the end of the road. In the event that the turtle collides with any of the cars, it would be game over. 

## The folders are:
- myCode
- solutionCode

myCode folder consist of the original code that I used for this turtle crossy-road program. 
solutionCode folder consist of the code which is the solution by the course instructor Dr Angela Yu used for this program. 

## Folder contents:

Both these folder contains files of the same name as well as same functionality. These files are:

- main.py.  
- player.py. 
- scoreboard.py
- car_manager.py

<ins>main.py</ins> is where the code is run such that the entire program can run.

<ins>player.py</ins> is where the class Player(Turtle) resides and it inherits some properties from the Turtle module. Furthermore, it contains various methods such as:

- up(self) allows the turtle to move forward whenever the up key is pressed.
- go_to_start(self) allows the turtle to return back to its original starting point once the level is complete.
- is_at_finish_line(self) allows returns a boolean value and is used to indicate whether the turtle has successfully reached the end of the level or not.

<ins>scoreboard.py</ins> is where the class Scoreboard(Turtle) resides and it inherits properties from the Turtle module. Furthermore it contains various methods such as:

- update_scoreboard(self) is used to indicate the level the player is currently on.
- increase_level(self) is used to change the level of the player once the player has successfully crossed the finish line.
- game_over(self) is used to indicate a game over in the event that the turtle collides with the car.

<ins>car_manager.py</ins> is file that contains the CarManager() class and is used to ensure that the program produces cars that move as well as increase the speed of the cards accordingly as the player levels up. It utilises the following methods which are:
- create_car(self) that creates cars of random colors such that they start coming from the right
- move_cars(self) is the method that ensures that the cars move in the leftwards direction.
- level_up(self) is the method that ensures that controls the current speed of the cars. As the player levels up, the car speed shall increase accordingly.
