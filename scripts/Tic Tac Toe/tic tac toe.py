from tkinter import *
import tkinter.messagebox
from random import *
import random
def single_player():
    tk = Tk()
    tk.title("Tic Tac Toe SINGLEPLAYER")
    global bclick, flag, player2_name, player1_name, playerb, pa,list1,fg,flag1,pm,pe
    pe = StringVar()
    playerb = StringVar()
    p1 = StringVar()
    list1=[1,2,3,4,5,6,7,8,9]
    fg=0
    flag1=0

    player1_name = Entry(tk, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=8)
    #playerb = player2_name.get() + " Wins!"
    pe =  player1_name.get() + " Wins!"
     
    #print(pm)
            

     
    bclick=True
    flag = 0

    def disableButton():
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
     
    def search(r):
        for i in list1:
            if i==r:
                return True
        else:
            return False
            
    def ran():
        return random.choice(list1)
    def btn1(self,x):
        global flag1
        if search(x):
            print(x)
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        
        checkForWin()
        if fg==1:
            kw(ran())
    def btn2(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        
        checkForWin()
        if fg==1:
            kw(ran())
    def btn3(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        
        checkForWin()
        if fg==1:
            kw(ran())
    def btn4(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        
        checkForWin()
        if fg==1:
            kw(ran())
    def btn5(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        
        checkForWin()
        if fg==1:
            kw(ran())
    def btn6(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        checkForWin()
        if fg==1:
            kw(ran())
    def btn7(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        checkForWin()
        if fg==1:
            kw(ran())
    def btn8(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        checkForWin()
        if fg==1:
            kw(ran())
    def btn9(self,x):
        global flag1
        if search(x):
            self["text"]="X"
            list1.remove(x)
            fg=1
            flag1=flag1 +1
        else:
            self["text"]="O"
            flag1=flag1 +1
        
        checkForWin()
        if fg==1:
            kw(ran())
        
    def kw(r):
        print(flag1)
        if r==1:
            list1.remove(r)
            fg=0
            button1.invoke()
        elif r==2:
            list1.remove(r)
            fg=0
            button2.invoke()
        elif r==3:
            list1.remove(r)
            fg=0
            button3.invoke()
        elif r==4:
            list1.remove(r)
            fg=0
            button4.invoke()
        elif r==5:
            list1.remove(r)
            fg=0
            button5.invoke()
        elif r==6:
            list1.remove(r)
            fg=0
            button6.invoke()
        elif r==7:
            list1.remove(r)
            fg=0
            button7.invoke()
        elif r==8:
            list1.remove(r)
            fg=0
            button8.invoke()
        elif r==9:
            list1.remove(r)
            fg=0
            button9.invoke()
    
    
        
        checkForWin()
    def checkForWin():
        global pe
        if (button1['text'] == 'X' and button2['text'] == 'X' and
        button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and
        button6['text'] == 'X' or
            button7['text'] =='X' and button8['text'] == 'X' and
        button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and
        button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and
        button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and
        button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and
        button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and
        button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and
        button9['text'] == 'X'):
            disableButton()
            
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "YOU WON!")
            tk.destroy()
            
                

        elif(flag1 == 9):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
            tk.destroy()

        elif (button1['text'] == 'O' and button2['text'] == 'O' and
button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and
button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and
button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and
button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and
button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and
button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and
button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and
button9['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and
button9['text'] == 'O'):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", 'COMPUTER WINS!')
            tk.destroy()
        
            
        
        
        
   
        
        
    
            
        
    label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white',
    fg='black', height=1, width=8)
    label.grid(row=1, column=0)


   

    button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn1(button1,1))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn2(button2,2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn3(button3,3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn4(button4,4))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn5(button5,5))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn6(button6,6))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn7(button7,7))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn8(button8,8))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btn9(button9,9))
    button9.grid(row=5, column=2)

    tk.mainloop()



def multi_player():
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe multiplayer")
    global bclick, flag, player2_name, player1_name, playerb, pa
    pa = StringVar()
    playerb = StringVar()
    p1 = StringVar()
    p2 = StringVar()

    player1_name = Entry(tk, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=8)
    player2_name = Entry(tk, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=8)
    
            

     
    bclick=True
    flag = 0

    def disableButton():
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)
    def normalButton():
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        button1["state"] = NORMAL
        
    def TF():
        if len(player1_name.get()) == 0 and len(player2_name.get())==0:
            return False
        else:
            return True
        
    



    def btnClick(buttons):
        
        global bclick, flag, player2_name, player1_name, playerb, pa
        #print(p1.get())
        #print(p2.get())
        if(TF()):
            if buttons["text"] == " " and  bclick == True:
                buttons["text"] = "X"
                bclick = False
                playerb = player2_name.get() + " Wins!"
                pa =  player1_name.get() + " Wins!"
                checkForWin()
                flag += 1


            elif buttons["text"] == " " and bclick == False:
                buttons["text"] = "O"
                bclick = True
                checkForWin()
                flag += 1
            else:
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
        else:
            #disableButton()
            tk.destroy()
            tkinter.messagebox.showinfo("Tic-Tac-Toe","please fill player name before starting the Game")
            #normalButton()

    def checkForWin():
        if (button1['text'] == 'X' and button2['text'] == 'X' and
        button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and
        button6['text'] == 'X' or
            button7['text'] =='X' and button8['text'] == 'X' and
        button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and
        button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and
        button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and
        button3['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and
        button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and
        button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and
        button9['text'] == 'X'):
            disableButton()
            tk.destroy()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

        elif(flag == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
            tk.destroy()

        elif (button1['text'] == 'O' and button2['text'] == 'O' and
button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and
button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and
button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and
button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and
button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and
button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and
button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and
button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and
button9['text'] == 'O'):
            disableButton()
            tk.destroy()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


    buttons = StringVar()

    label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white',
    fg='black', height=1, width=8)
    label.grid(row=1, column=0)


    label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white',
    fg='black', height=1, width=8)
    label.grid(row=2, column=0)

    button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
    fg='white', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)

    tk.mainloop()



def main():
    root = Tk()
    
    root.geometry('400x500')
    root.title("Tic Tac Toe ")
    button_mp=Button
    f=Frame(root,height=70,width=1200,bg='crimson')
    #f.propagate(0)
    f.pack()
    
    h=Frame(root,height=70,width=1200)
    #f.propagate(0)
    h.pack()
    g=Frame(root,width=1200)
    #f.propagate(0)
    g.pack()
    v=Frame(root,width=1200)
    #f.propagate(0)
    v.pack()
    q=Label(v,text='TAP HERE TO PLAY MULTIPLAYER',fg='red',height=3)
    q.pack()
    
    k=Frame(root,width=1200)
    #f.propagate(0)
    k.pack()
    m=Frame(root,width=1200)
    #f.propagate(0)
    m.pack()
    i=Label(m,text='TAP HERE TO PLAY SINGLEPLAYER',fg='red',height=3)
    i.pack()
    
    button2=Button(g,bg='lightblue', height=2, width=20,text='Multiplayer',fg='red',bd=3,command=multi_player)
    #button2.place(bordermode=INSIDE)
    button2.grid(row=3,column=1)
    
     
    button3=Button(k,bg='lightblue', height=2, width=20,text='single player',fg='red',bd=3,command=single_player)
    #button2.place(bordermode=INSIDE)
    button3.grid(row=3,column=1)
    
    root.mainloop()
    
main()    
    