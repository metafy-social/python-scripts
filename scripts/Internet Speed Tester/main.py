from tkinter import *
from speedtest import Speedtest

root = Tk()
root.title("Internet Speed Checker")
root.geometry('1920x1080')
root.resizable(True,True)

def get_speed():
    speed = Speedtest()
    download = speed.download()
    upload = speed.upload()
    ping = speed.results.ping
    download_speed = round(download / 8 / 1024 / 1024,2)
    upload_speed = round(upload / 8 / 1024 / 1024,2)
    ping = round(ping, 2)
    down_lab.config(text='Download Speed : ' + str(download_speed) + " Mbps")
    upload_lab.config(text='Upload Speed : ' + str(upload_speed) + " Mbps")
    ping_lab.config(text='Ping : ' + str(ping) + " ms")

fg = '#0cc6a9'
bg = '#ed4947'  

title = Label(root, text="Internet Spped Tester",fg=fg, font=("Ubuntu",24,"bold"))

test_btn = Button(root, text="Get Speed",font=('Helvetica',32,'bold'),command=get_speed,bg=bg)
test_btn.place(x=800, y=700)

down_lab = Label(root,text='',fg=fg,font=('Ubuntu',24,'bold'))
down_lab.place(x=800, y = 100)

upload_lab = Label(root,text='',fg=fg,font=('Ubuntu',24,'bold'))
upload_lab.place(x=800, y = 300)

ping_lab = Label(root,text='',fg=fg,font=('Ubuntu',24,'bold'))
ping_lab.place(x=800, y = 500)

root.mainloop()
