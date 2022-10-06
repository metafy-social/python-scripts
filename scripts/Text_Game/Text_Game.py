import random
import time
import sys

def start():
    print('Hello you r in the future and r fighting a robot')
    time.sleep(3)
    print('you dont know what to do, thats why im here')
    time.sleep(3)
    print('I am a Simulated Artificial Machine but u can call me S.A.M.')
    smileyface()

def smileyface():
    time.sleep(0.3)
    print('__________________ ')
    time.sleep(0.3)
    print('|                |')
    time.sleep(0.3)
    print('|  @        @    |')
    time.sleep(0.3)
    print('|       !        |')
    time.sleep(0.3)
    print('|   \_______/    |')
    time.sleep(0.3)
    print('|________________|')



def level1():
    a = ''
    while a != 'run away' and a != 'shoot robot in head':
        a = input('u can currently do two things which is either run away or shoot robot in head, what do u choose: ')
        if a == 'run away':
            time.sleep(3)
            print('Unfortunately you have now been hunted down by an army of robots and have been executed')    
            time.sleep(3)
            print('too bad')
            res = input('Do you wanna restart: ')
            if res == 'yes':
                start()
                level1()
                path()
                again = choice()
                wtf(again)
            else:
                print('bye')
                sys.exit()       
        elif a == 'shoot robot in head':
            time.sleep(3)
            print('Congratulations you shot the robot in the head and are not dead!!')
            

def path():
    time.sleep(3)
    print('You are running away from the robots but...')
    time.sleep(3)
    print('there is a dangerous path of an army of robots coming your way')
    time.sleep(3)
    print('you have got two paths that you can go down')
    time.sleep(3)
    print('but you have to decide which one is the correct one since one of them is a dead end')
    time.sleep(3)
    print('choose wisely!!!!!!! ')
    print()

def choice():
    d = ''
    while d != '1' and d != '2':
        time.sleep(1)
        d = input('So which one do you want to go on, path 1 or 2: ')
    return d

def wtf(rightpath):
    t = random.randint(1,2)
    if rightpath == str(t):
        time.sleep(3)
        print('good you went down the correct path and cheated death!!')  
    else:
        time.sleep(3)
        print('oh no you have been spotted by the robots!!!')
        time.sleep(3)
        print('and you have been shot multiple time and are now dead.')


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    start()
    level1()
    path()
    again = choice()
    wtf(again)
    time.sleep(1)
    playAgain = input("""Do you want to play again? 
    Type yes or y to play again and no or n if you want to stop: """)