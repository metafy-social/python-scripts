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
    canvas.after_cancel(timer)
    text_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8 == 0:
        text_label.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps%2 == 0:
        text_label.config(text="Short Break", fg=PINK)
        countdown(short_break_sec)
    else:
        text_label.config(text="Work", fg=GREEN)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            checkmark.config(text=mark, fg=GREEN, bg=YELLOW)


# -------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
text_label.grid(row=0, column=1)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

start_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
start_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

canvas.grid(column=1, row=1)

window.mainloop()
