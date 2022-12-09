#import asyncio
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile 
from time import sleep
import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os,sys
#import re
from tkinter import *
import subprocess
import threading
import requests
from bs4 import BeautifulSoup as bs
import time
from bottle import route, run

#import pyperclip 'http://192.168.43.1:8080/'
def sync():
   
    url=entry.get()
    #url='http://192.168.43.147:8080/'
    entry.delete(0, tkinter.END)
    entry.insert(0,"connected!!! syncing to %s"%url )
    while True:
    #try:
        global stop
        
        
        c=requests.get(url)
        if c.status_code==200:
            print("connected!!! syncing to %s"%url,end="\r")
            
        else:
            print('tell your friend to run sync_clipboard_to_pc.py in mobile :)')
            break
        pr=c.text
        soup=bs(pr,'html.parser')
        mobile_text=soup.find('h1')
        hs=mobile_text.text
        
        pk=win.clipboard_get()
        if pk not in hs:
            print('i think you copied from your computer so i stop for 5 sec paste it in 2 sec')
            time.sleep(5)
        win.clipboard_clear()   
        win.clipboard_append(hs)
        if stop==1:
            print("i am stopped.....")
            break
    #except:
        #print('please tell your friend to run sync_clipboard_to_pc.py in mobile :)')
        #break






def stop():
    
    # Assign global variable and set value to stop
    global stop
    entry.delete(0, tkinter.END)
    entry.insert(0, 'i am stoped......')
    stop = 1
def exiit():
    win.destroy()
def start_sync(event):
    global start_thread
    global stop
    stop=0
    start_thread = threading.Thread(target=sync)
    start_thread.deamon=True
    start_thread.start()
win=Tk()
win.geometry("400x200")
laable=ttk.Button(win,text='start syncing',command=lambda :start_sync(None))
laable.pack()

stop = ttk.Button(win, text="Stop syncing",command=stop)
stop.pack()
entryText = tkinter.StringVar()
entry = ttk.Entry( win, textvariable=entryText,width=50 )
entry.pack()

button = ttk.Button(text = "Click and Quit", command = exiit)
button.pack()

win.mainloop()
os._exit(0)
