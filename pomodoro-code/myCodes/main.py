from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    # reset check_marks
    checkmarks.config(text=(math.floor(reps / 2) + 1) * "✓️")
    # timer_text 00:00
    canvas.itemconfig(timer_text, text=f"00:00")
    # title_label "Timer"
    timer_display.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        # If it's the 8th rep:
        count_down(long_break_sec)
        # Red break
        timer_display.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # If it's the 2nd/4th/6th rep:
        count_down(short_break_sec)
        # Pink break
        timer_display.config(text="Break", fg=PINK)
    else:
        # If it's the 1st/3rd/7th rep:
        count_down(work_sec)
        # Green work
        timer_display.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # For every 2 reps checkmark will get added
        checkmarks.config(text=(math.floor(reps / 2) + 1) * "✓️")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=500)
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Labels
timer_display = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_display.grid(column=1, row=0)

# Tomato icon
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
# button.pack(side="left")
start_button.grid(column=0, row=2)

# Reset Button

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
# button.pack(side="left")
reset_button.grid(column=2, row=2)

# Green tick

checkmarks = Label(text="✓️", fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
