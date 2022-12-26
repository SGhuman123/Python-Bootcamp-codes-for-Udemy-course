# Description of Snake Game


In this folder it has my original code in the myCode folder and the solution code in the providedSol folder.
</br>
Within both folders there contain the following files:
- main.py
- food.py
- scoreboard.py
- snake.py

In main.py here is where the code is run such that the game can function. It is the file that links to all other files.

In food.py this is the file that contains the class Food and it inherits some of the properties from the turtle class through inheritance. The refresh method in the class sets the position of the food randomly through the use of the random module.

In scoreboard.py this is the file responsible for displaying the scoreboard of the game as well as updating the scoreboard whenever the snake touches the food and signalling when the game is over which can happen in scenarios where the snake eats itself or collides with the wall.

In snake.py this is the file that is responsible for creating the borders though the create_border() and create_borders() functions. Moreover, this is also the file which has the Snake() class and contains various methods namely:
- create_snake(self). This method is responsible for creating the initial starting snake body when the game just begins
- add_segment(self)
- extend(self). This method is responsible for extending the snake body everytime it eats a food.
- up(self). This method is responsible for ensuring that the snake is travelling in an upwards direction if it is already not.
- down(self). This method is responsible for ensuring that the snake is travelling in an downawards direction if it is already not.
- right(self). This method is responsible for ensuring that the snake is travelling in an rightwards direction if it is already not.
- left(self). This method is responsible for ensuring that the snake is travelling in an leftwards direction if it is already not.

Here is a short-clip how my code works:

https://user-images.githubusercontent.com/63066897/209571166-789df678-ec4d-4e24-857d-7d3e151582e0.mov
