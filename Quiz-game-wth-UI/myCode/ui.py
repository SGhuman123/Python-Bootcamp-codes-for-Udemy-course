from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        # Setup the background
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Set up the score label
        self.score_display = Label(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}", font=("Arial", 20),
                                   fg="white", bg=THEME_COLOR)
        self.score_display.grid(column=1, row=0)

        # Set up the display card (Canvas)
        self.canvas = Canvas(bg="white", highlightthickness=0, width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="This is how we do it", fill="black",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        # Set up the green tick button
        self.green_button_img = PhotoImage(file="images/true.png")
        self.green_button_img_button = Button(image=self.green_button_img, highlightthickness=0,
                                              highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.green_button_img_button.grid(column=0, row=2)

        # Set up the red cross button
        self.red_button_img = PhotoImage(file="images/false.png")
        self.red_button_img_button = Button(image=self.red_button_img, highlightthickness=0,
                                            highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.red_button_img_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_display.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz!!!")
            self.green_button_img_button.config(state="disabled")
            self.red_button_img_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
