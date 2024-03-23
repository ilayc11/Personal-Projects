from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    countDown(work_sec)
    if reps%8==0:
        countDown(long_break_sec)
        title_label.config(text="Long Break",fg=GREEN)
    elif reps%2==0:
        countDown(short_break_sec)
        title_label.config(text="Short Break",fg=PINK)
    else:
        countDown(work_sec)
        title_label.config(text="Work",fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    count_min=count // 60
    count_sec= count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,countDown,count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

title_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
title_label.grid(column=1,row=0)

canvas = Canvas(width=200, height=230,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)




start_bt=Button(text="Start",highlightthickness=0,command=start_timer)
reset_bt=Button(text="Reset",highlightthickness=0)
start_bt.grid(column=0,row=2)
reset_bt.grid(column=2,row=2)


checkMaRKS=Label(text="✔",fg=GREEN,bg=YELLOW)
checkMaRKS.grid(column=1,row=3)
window.mainloop()
