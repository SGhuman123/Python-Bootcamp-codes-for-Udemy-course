from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- EXTRACT DATA ------------------------------- #

# next time program is run it should use words_to_learn.csv otherwise,
# it should use french_words.csv instead
try:
    with open("words_to_learn,csv") as file:
        data_from_csv = file.read()
except FileNotFoundError:
    data_from_csv = pandas.read_csv("data/french_words.csv")
french_list_of_words = data_from_csv.to_dict(orient="records")
print(french_list_of_words)

# ---------------------------- CHANGE WORDS  ------------------------------- #
current_word = {}
please_speed_up = False


# When green or red button is clicked
def speed_up():
    global please_speed_up, current_word
    please_speed_up = True
    current_word = random.choice(french_list_of_words)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)


# When green or red button is not clicked
def change_word():
    global current_word, please_speed_up
    current_word = random.choice(french_list_of_words)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    if please_speed_up:
        please_speed_up = False
    window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD  ------------------------------- #


def flip_card():
    global current_word
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")
    window.after(3000, func=change_word)


# ---------------------------- I KNOW THE WORD  ------------------------------- #


def i_know_the_current_word():
    # word should be removed from current list of words.
    global french_list_of_words

    french_list_of_words = [val for val in french_list_of_words if not (val["French"] == current_word["French"])]
    # words I don't know should be saved to words_to_learn.csv
    with open("words_to_lean.csv", mode="w") as words_to_learn:
        result = "French,English\n"
        for value in french_list_of_words:
            result += f"{value['French']},{value['English']}\n"
        words_to_learn.write(result)
    speed_up()


# ---------------------------- UI SETUP ------------------------------- #

# Set up the background
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set up the flashcard/button
# Create a canvas for the buttons and the words
canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=old_image)
language_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Red cross button
red_cross_img = PhotoImage(
    file="images/wrong.png")
red_cross_img_button = Button(image=red_cross_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                              command=speed_up)
red_cross_img_button.grid(column=0, row=1)

# Green tick button
green_tick_img = PhotoImage(
    file="images/right.png")
green_tick_img_button = Button(image=green_tick_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                               command=i_know_the_current_word)
green_tick_img_button.grid(column=1, row=1)

change_word()

window.mainloop()
