from password_strength import PasswordStats
import tkinter as tk
import math
from tkinter import messagebox


def check():
    if entry.get() == "":
        messagebox.showinfo("Error", "Password Can't be empty")
    else:
        result = PasswordStats(entry.get())
        final = result.strength()
        label1["text"] = str(math.ceil(final*100)) + " %"
        if final >= 0.66:
            w.create_rectangle(105, 50, 300, 100,
                               fill="#27cf54", outline="white")
        elif final > 0.10 and final < 0.65:
            w.create_rectangle(105, 50, 300, 100,
                               fill="#f0f007", outline="white")
        elif final <= 0.10:
            w.create_rectangle(105, 50, 300, 100,
                               fill="#de3c3c", outline="white")


window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x400")
label1 = tk.Label(window, text="")
label1.place(x=200, y=275)
head = tk.Label(window, text="Password Strength calculator",
                font=("helvetica", 15, "bold"))
head.pack(ipadx=12, ipady=12)
label = tk.Label(window, text="Enter Your Password",
                 font=("helvetica", 10, "bold"))
label.pack(ipadx=5, ipady=5)
entry = tk.Entry(window)
entry.pack(ipadx=30, ipady=5)
button = tk.Button(window, text="check", command=check)
button.pack(ipadx=5, ipady=5)
w = tk.Canvas(window, height=100, width=600)
w.pack()


window.mainloop()
