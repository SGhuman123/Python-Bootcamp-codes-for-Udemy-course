class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct_questions = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.correct_questions += 1
            self.score()
        else:
            print("That's wrong.")
            print(f'The correct answer was: {correct_answer}')
            self.score()

    def score(self):
        number_of_questions_answered = self.question_number
        number_of_questions_answered_correctly = self.correct_questions
        print(f"Your current score is: {number_of_questions_answered_correctly}/{number_of_questions_answered}")
