from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary


root = Tk()
root.title("GUI Dictionary")
root.geometry("500x400")


dictionary = PyDictionary()


def getMeaning():
    response = dictionary.meaning(word.get())
    if (response):
        if ('Noun' in response):
            meaning = response['Noun'][0]
        elif ('Verb' in response):
            meaning = response['Verb'][0]
        elif ('Adjective' in response):
            meaning = response['Adjective'][0]
        else:
            meaning = "Invalid word"
    else:
        messagebox.showinfo(
            "Error", "Please add a Noun, Pronoun, verb or a valid word.")
    meaning_label.config(text=meaning)



heading_label = Label(root, text="DICTIONARY", font=("Times 35 bold"), foreground='dark blue')
heading_label.config(anchor=CENTER)
heading_label.pack(pady=10)


frame = Frame(root)
Label(frame, text="Enter Word", font=("Helvetica 15 bold"), foreground='dodger blue').pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack(padx=10)
frame.pack()

search_button = Button(root, text="Search Word", font=("arial 15 bold"), relief=RIDGE, borderwidth=3, cursor="hand2", foreground='Magenta', command=getMeaning)
search_button.config(anchor=CENTER)
search_button.pack(pady=10)


frame1 = Frame(root)
Label(frame1, text="Meaning : ", font=("Helvetica 15 bold"), foreground='medium turquoise').pack(side=LEFT)
meaning_label = Label(frame1, text="", font=("Helvetica 12"))
meaning_label.pack(pady=5)
frame1.pack(pady=10)

root.mainloop()