# Provided solutions for the Quiz-game (without UI) project

This is my solution to the Quiz-game project.
</br>
</br>

main.py
</br>
Contains is the file that links all the other files (data.py, question_model.py, quiz_brain.py) together and where the code is run such that the entire program can run.
</br>
</br>

data.py
</br>
This file contains all the data for the questions as well as the answers to the questions.
</br>
</br>

question_model.py
</br>
This file contains class Question which allows the questions and theor data to be structured in the manner I wish.
</br>
</br>
quiz_brain.py
</br>
This file contains the class QuizBrain that consist of 4 methods. There are:
- still_has_questions(self) method that checks if there are still any unanswered questions.
- next_question(self) method that brings in the next question after the current question has been answered
- check_answer(self, user_answer, correct_answer) method that verifies if the user's inputed answer is correct or not.
- score(self) method that helps update the scorecard of the user as he or she answer the questions.
</br>
