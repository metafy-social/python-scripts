# # import required packages

import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
import tkcalendar
  
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('500x250')

def printInput():

    # getting Stock Data
    msft = yf.Ticker(inputtxt.get(1.0))
    a = msft.history(start=start_date.get_date(), end=end_date.get_date())
    
    # ploting graph
    mpf.plot(a, type='candle', volume=True, title = inputtxt.get(1.0))
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 2,
                   width = 25
                    )
inputtxt.pack()


start_date = tkcalendar.DateEntry(frame, text = "Start Date")
start_date.pack(padx=10,pady=10)

end_date = tkcalendar.DateEntry(frame, text = "End Date")
end_date.pack(padx=10,pady=10)



# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()