import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile, askdirectory
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("Docx to PDF Converter")


def openfile():
    file = askopenfile(filetypes=[("Word Files", "*.docx")])
    convert(file.name)
    showinfo("Done", "File Converted Successfully")


def openfolder():
    folder = askdirectory()
    convert(folder)
    showinfo("Done", "Files Converted Successfully")


label = tk.Label(win, text="Select File/Folder to convert: ")
label.grid(row=0, column=0, padx=5, pady=5)

button1 = ttk.Button(win, text="Select File", width=30, command=openfile)
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = ttk.Button(win, text="Select Folder", width=30, command=openfolder)
button2.grid(row=2, column=0, padx=5, pady=5)

win.mainloop()
