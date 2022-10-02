from tkinter import *
import random
import tkinter
 
# main root
root = Tk()
root.title('Type Speed Test')

# the geometry of the window
root.geometry('700x700')

# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            labelRight.configure(text=labelRight.cget('text')[1:])
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


def resetWritingLabels():
    # Text List
    possibleTexts = [
        'The fact that theres a stairway to heaven and a highway to hell explains life well. The Great Dane looked more like a horse than a dog. Barking dogs and screaming toddlers have the unique ability to turn friendly neighbors into cranky enemies. The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it. Fluffy pink unicorns are a popular status symbol among macho men. There was no telling what thoughts would come from the machine. She cried diamonds. He excelled at firing people nicely. Its never been my responsibility to glaze the donuts. Everyone pretends to like wheat until you mention barley. The body piercing didnt go exactly as he expected',
        'She saw no irony asking me to change but wanting me to accept her for who she is. The quick brown fox jumps over the lazy dog. The blinking lights of the antenna tower came into focus just as I heard a loud snap. He decided to count all the sand on the beach as a hobby. Im not a party animal, but I do like animal parties. The gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms. He told us a very exciting adventure story. She was too busy always talking about what she wanted to do to actually do any of it. She was amazed by the large chunks of ice washing up on the beach. After coating myself in vegetable oil I found my success rate skyrocketed. You have no right to call yourself creative until you look at a trowel and think that it would make a great lockpick.',
        'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
    ]
    text = random.choice(possibleTexts).lower()
    splitPoint = 0
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False
    
    amountWords = len(labelLeft.cget('text').split(' '))
    
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    ResultLabel.destroy()
    ResultButton.destroy()

    resetWritingLabels()

def addSecond():

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    if writeAble:
        root.after(1000, addSecond)
resetWritingLabels()
root.mainloop()