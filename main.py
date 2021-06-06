import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycle = 1
timer = None
check_mark = ""
window = Tk()
window.config(padx=50, pady=50)
window["bg"] = YELLOW
window.title("MY TIMER")


def timer_count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(main_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, timer_count_down, count-1)
    else:
        global check_mark
        for _ in range(int(cycle/2)):
            check_mark += "✔"
        label_check.config(text=f"{check_mark}")
        start_timer()


def start_timer():
    work_seconds = 60*WORK_MIN
    short_break_seconds = 60*SHORT_BREAK_MIN
    long_break_seconds = 60*LONG_BREAK_MIN
    global cycle
    if cycle % 8 == 0:
        main_seconds = long_break_seconds
        label.config(text="BREAK", fg=PINK)
    elif cycle % 2:
        main_seconds = work_seconds
        label.config(text="WORK", fg=RED)
    else:
        main_seconds = short_break_seconds
        label.config(text="BREAK", fg=GREEN)
    cycle += 1
    timer_count_down(main_seconds)


def reset_time():
    global cycle, check_mark
    cycle = 1
    check_mark = ""
    window.after_cancel(timer)
    label_check["text"] = ""
    label["text"] = "TIMER"
    canvas.itemconfig(main_timer, text="00:00")


label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=1, column=2)
canvas = Canvas(window, height=250, width=250, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(117, 120, image=photo)
main_timer = canvas.create_text(115, 115, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=3, column=2)
button_start = Button(text="start", command=start_timer)
button_start.grid(row=4, column=1)
button_reset = Button(text="reset", command=reset_time)
button_reset.grid(row=4, column=3)
label_check = Label(bg=YELLOW, fg=GREEN)
label_check.grid(row=4, column=2)
window.mainloop()
