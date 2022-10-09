import random
t = 0
g = int(input("Total Guesses: "))
low = int(input("Enter the lower range: "))
high = int(input("Enter the upper range: "))
x = random.randint(low, high)
n = int(input("Enter an integer between the given range: "))
 
while (x != 'n'):
    if(t<(g-1)):
        if n < x:
            print("The number guessed is low")
            t = t+1
            n = int(input("Enter an integer between the given range: "))
        elif (n > x):
            print("The number guessed is high")
            t = t+1
            n = int(input("Enter an integer between the given range: "))
        else:
            print("The number guessed is right")
            print("Total guesses taken: ", t+1)
            break
    else:
        print("Ran out of tries!")
        break