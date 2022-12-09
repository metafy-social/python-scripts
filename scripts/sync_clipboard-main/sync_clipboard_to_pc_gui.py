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

from bottle import route, run
import os,subprocess,re
#import pyperclip
def sync():
    laable.configure(text="started")
    laable.configure(command='')
    d=''

    if os.name =='linux':
        
        #do
        df=subprocess.getoutput('ifconfig')
        ip=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').findall(df)
        for i in ip:
            if i.startswith('192'):
                d+=i
                break
        
    elif os.name =='posix':
        
        df=subprocess.getoutput('ifconfig')
        ip=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').findall(df)
        for i in ip:
            if i.startswith('192'):
                d+=i
                break

        
    elif os.name=='darwin':
        #do
        
        df=subprocess.getoutput('ifconfig')
        ip=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').findall(df)
        for i in ip:
            if i.startswith('192'):
                d+=i
                break
        
    elif os.name=='nt':
        #do
        
        df=subprocess.getoutput('ipconfig')
        ip=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').findall(df)
        for i in ip:
            if i.startswith('192'):
                d+=i
                break


    @route('/')
    def hello():
        #g=pyperclip.paste()
        return '''<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="10">
</head>
<body>

<h1 color='blue'>%s</h1>

</body>
</html>

'''%win.clipboard_get()


    #os.system('python -m http.server 8080')
    entryText = tkinter.StringVar()
    entry.delete(0, tkinter.END)
    entry.insert(0, 'running on >> http://%s/8080/'%d)
    #entryText.set('running on >> http://%s/8080/'%d)
    run(host=d, port=8080, debug=True)
    

def start_sync(event):
    global start_thread
    start_thread = threading.Thread(target=sync)
    start_thread.deamon=True
    start_thread.start()
def exiit():
    win.destroy()

    
win=Tk()
win.geometry("400x200")
laable=ttk.Button(win,text='start syncing',command=lambda :start_sync(None))
laable.pack()
entryText = tkinter.StringVar()
entry = ttk.Entry( win, textvariable=entryText,width=50 ,state="rw")
entry.pack()

button = ttk.Button(text = "Click and Quit", command = exiit)
button.pack()

win.mainloop()
os._exit(0)
