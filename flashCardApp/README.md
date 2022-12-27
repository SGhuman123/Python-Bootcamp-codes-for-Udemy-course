# Description

https://user-images.githubusercontent.com/63066897/209700430-27efd4a1-1cae-4ab4-96b1-f7fd080e2457.mov


This flashcard app serves as a tool to help someone learn French.

## How it works:
1) If a user presses the green button then it suggest that the user knows the word and the program shall proceed to the next French word.
2) If the user clicks the red button or gives no response after 3 seconds time interval then the program shall take that the user does not know the word and it shall be saves in the csv file known as words_to_learn.csv

## Folder descriptions:

- myCode: This is my own personal code of the flashcard app.
- providedCode: This is the provided code of the flashcard app by Dr Angela Yu. 


## myCode Folder description:

- data: This folder contains the french_words.csv file where main.py reads off the French words and English meaning
- images: This folder contains the following images which are card_back.png, card_front.png, right.png, wrong.png to act as the graphics for the GUI program.
- main.py: This is where all the python code is run and it uses the pandas module to read the data and structure it in a nice format. It also uses the tkinter module to provide the graphics for the GUI. Lastly, it uses the random module to generate the random words from the french_words.csv in a random sequence.
- Lastly words, that the user gets wrong are stored in the file words_to_learn.csv

## providedCode

- data: This folder contains the french_words.csv file where main.py reads off the French words and English meaning
- images: This folder contains the following images which are card_back.png, card_front.png, right.png, wrong.png to act as the graphics for the GUI program.
- main.py: This is where all the python code is run and it uses the pandas module to read the data and structure it in a nice format. It also uses the tkinter module to provide the graphics for the GUI. Lastly, it uses the random module to generate the random words from the french_words.csv in a random sequence.
- Lastly words, that the user gets wrong are stored in the file words_to_learn.csv







