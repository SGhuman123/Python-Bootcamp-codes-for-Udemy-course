# Description

Here are the code solutions provided by the course instructor Dr Angela Yu.


## Provided solutions for the Quiz-game (with UI) project
This is the provided solution to the Quiz-game project.

main.py Contains is the file that links all the other files (data.py, question_model.py, quiz_brain.py) together and where the code is run such that the entire program can run.

data.py This file contains all the data for the questions as well as the answers to the questions.

question_model.py This file contains class Question which allows the questions and theor data to be structured in the manner I wish.

quiz_brain.py This file contains the class QuizBrain that consist of 4 methods. There are:

- still_has_questions(self) method that checks if there are still any unanswered questions.
- next_question(self) method that brings in the next question after the current question has been answered
- check_answer(self, user_answer, correct_answer) method that verifies if the user's inputed answer is correct or not.
- score(self) method that helps update the scorecard of the user as he or she answer the questions.

ui.py This file contains the class QuizInterface(). This class consist of various methods such as:

- get_next_question(self). This causes the UI to change to the next question.
- true_pressed(self). This is activated when the user clicks on the true button.
- false_pressed(self). This is activated when the user clicks on the false button.
- give_feedback(self). This helps check if what the user clicks on is indeed the correct answer or not and will cause the user-interface to change accordingly.
