import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# def get_mouse_click_coordinate(x, y):
#     print(x, y)


# To retrieve and read csv data
data = pandas.read_csv("50_states.csv")
state_and_coordinates = {}

dictionary_data = data.to_dict()
index_number = 0
states_to_learn = []

while index_number < 50:
    states_to_learn.append(dictionary_data["state"][index_number])
    state_and_coordinates[dictionary_data["state"][index_number]] = (
        dictionary_data["x"][index_number], dictionary_data["y"][index_number])
    index_number += 1

print(state_and_coordinates)
number_of_correct_states = 0
number_of_questions = 0
while number_of_correct_states < 50:
    wer_state = screen.textinput(title=f"{number_of_correct_states}/50 States Correct",
                                 prompt="What's another state's name?").title()
    if wer_state == "Exit":
        break
    elif wer_state in states_to_learn:
        # print(states_to_learn)
        # states_to_learn.pop(wer_state)
        writer.goto(state_and_coordinates[wer_state])
        writer.write(wer_state)
        number_of_correct_states += 1
        states_to_learn.remove(wer_state)
    number_of_questions += 1

# States that I don't know saved to csv
states_that_I_do_not_know = pandas.DataFrame(states_to_learn)
states_that_I_do_not_know.to_csv("states_to_learn.csv")

# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.exitonclick()
