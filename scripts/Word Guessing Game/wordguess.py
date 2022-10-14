import time
from random_word import RandomWords
r = RandomWords()
print("Welcome")

def main():
    global count
    global display
    global word
    global finalword
    global progress
    global length
    global playgame
    word = r.get_random_word()
    finalword = word
    length = len(word)
    count = 0
    display = '_' * length
    progress = []
    playgame = ""

def replay():
    play = input("Play again? [y/n]: ")
    if(play not in ["Y", "y", "N", "n"]):
        replay()    
    if(play == "y" or play == "Y"):
        main()
        execute()
    elif(play == "n" or play == "N"):
        exit()

def execute():
    global count
    global display
    global word
    global progress
    global playgame 
    lives = 10
    guess = input("Enter your guess: ")
    if guess in word:
        progress.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in progress:
        print("Already guessed, guess again")
    else:
        count += 1
        print("Wrong guess. " + str(lives-count) + " lives remaining")
        if(count == lives):
            time.sleep(1)
            print("You Die :(")
            print("Word: " + finalword)
            replay() 
    if(word == '_' * length)  :
        print("You Live! :)")
        replay()
    elif(count != lives):
        execute()

main()
execute()        