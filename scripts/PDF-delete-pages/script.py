from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename


win = tk.Tk()
win.geometry("400x200")
win.title("Delete PDF Pages")


def pagedel():
    pages_del = pages.get()
    pages_to_delete = pages_del.strip().split(",")
    pages_to_delete = [(int(i) - 1) for i in pages_to_delete]

    with open(path, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

    out_of_index_page = []
    for num in pages_to_delete:
        if num > num_pages:
            out_of_index_page.append(num)

    if len(out_of_index_page) == 0:

        infile = PdfFileReader(path, "rb")
        output = PdfFileWriter()

        for i in range(infile.getNumPages()):
            if i not in pages_to_delete:
                p = infile.getPage(i)
                output.addPage(p)

        inputfile_name = ((path.split("\\")[-1]).split(".pdf"))[0]

        output_name = inputfile_name + "_deleted.pdf"

        with open(output_name, "wb") as f:
            output.write(f)

        print(f"\nThe output pdf is saved as: {output_name}\n")

    else:
        print("\nPage number entered is greater than the No of Pages in PDF")
        print("Please Check & Re-Try\n")


def getpages():
    global pages, path
    user_path = askopenfilename().strip()
    path = os.path.normpath(user_path)

    label2 = ttk.Label(win, text="Enter page numbers to be deleted seperated by commas:\n(Eg: 1,2) ")
    label2.grid(row=0, column=0, padx=50, pady=20)

    pages = tk.Entry(win, width = 30)
    pages.grid(row=1, column=0, padx=50, pady=0)

    button2 = ttk.Button(win, text="Enter", width=30, command=pagedel)
    button2.grid(row=2, column=0, padx=50, pady=10)


label1 = ttk.Label(win, text="Select PDF File: ")
label1.grid(row=0, column=0, padx=100, pady=40)

button1 = ttk.Button(win, text="Select File", width=30, command=getpages)
button1.grid(row=1, column=0, padx=100, pady=0)

win.mainloop()
