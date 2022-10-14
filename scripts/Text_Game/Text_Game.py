import random
import time
import sys
# print(""" ──────────────────██
#             ▄───▄▀█▄▄▄▄
#             ─ ▄▀─█▄▄
#             ▄▄▄▀───▀▄
#             ▀────────▀▀ """)

def start():
    # story generated
    print('Hello you are in the future and are fighting a robot')
    time.sleep(3)
    print('you dont know what to do, thats why im here')
    time.sleep(3)
    print('I am a Simulated Artificial Machine but you can call me S.A.M.')
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


# First obstacle
def level1():
    question_one = ''
    while question_one != 'run away' and question_one != 'shoot robot in head':
        question_one = input('You can currently do two things which is either run away or shoot robot in head, what do you choose: ')
        
        #if chosen option and outcome of option
        if question_one == 'run away':
            time.sleep(3)
            print('Unfortunately you have now been hunted down by an army of robots and have been executed')    
            time.sleep(3)
            print('too bad')
            

            # restart for when user fails
            restart = input('Do you wanna restart: ')
            if restart == 'yes':
                start()
                level1()
                path()
                again = choice()
                random_select(again)
            else:
                print('bye')
                sys.exit()       
        
        elif question_one == 'shoot robot in head':
            time.sleep(3)
            print('Congratulations you shot the robot in the head and are not dead!!')
            

def path():
    # story generated
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

# Second obstacle
def choice():
    question_two = ''
    while question_two != '1' and question_two != '2':
        time.sleep(1)
        question_two = input('So which one do you want to go on, path 1 or 2: ')
    return question_two


# random path chosen for user to be right or wrong
def random_select(rightpath):
    select = random.randint(1,2)

    if rightpath == str(select):
        time.sleep(3)
        print('good you went down the correct path and cheated death!!')  
        level2()

    else:
        time.sleep(3)
        print('oh no you have been spotted by the robots!!!')
        time.sleep(3)
        print('and you have been shot multiple time and are now dead.')

def level2():
    time.sleep(3)
    print('You are running far away from the robots')

    time.sleep(2)
    print(""" ──────────────────██
                ▄───▄▀█▄▄▄▄
                ─ ▄▀─█▄▄
                ▄▄▄▀───▀▄
                ▀────────▀▀ """)

    time.sleep(3)
    print('and all of a sudden you see a cyborg in the distance')
    time.sleep(2)
    print("""░░░░░░░░░░░░░┌─────┐░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░│░▌░▌░│░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░│░▄▄░░│░░░░░░░░░░░░░░░░░░░░
░░░░░░░░┌─┬──┴─┬─┬─┴──┬─┐░░░░░░░░░░░░░░░
░░░░░░░░│░├┐░░░│░│░░░┌┤░│░░░░░░░░░░░░░░░
░░░░░░░░│░││░░░│░│░░░││░│░░░░░░░░░░░░░░░
░░░░░░░░│░││░░░├─┤░░░││░│░░░░░░░░░░░░░░░
░░░░░░░░└─┘├──┬┴─┴┬─┬┘└─┘░░░░░░░░░░░░░░░
░░░░░░░░░░░│░░│░░░│░│░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░│░░│░░░│░│░░░░░░░░░░░░░░░░░░░
░░░░░░░░░┌─┘░░│░░░│░└─┐░░░░░░░░░░░░░░░░░
░░░░░░░░░└────┘░░░└───┘░░░░░░░░░░░░░░░░░""")
    time.sleep(3)
    print('he has been sent to capture you and take you back to the robots!!!')

    time.sleep(3)
    print('three items are infront of you ')

    time.sleep(3)
    print("a mech suit")
    time.sleep(2)
    print("""───────────▄▄▄▄▄▄▄▄▄───────────
────────▄█████████████▄────────
█████──█████████████████──█████
▐████▌─▀███▄───────▄███▀─▐████▌
─█████▄──▀███▄───▄███▀──▄█████─
─▐██▀███▄──▀███▄███▀──▄███▀██▌─
──███▄▀███▄──▀███▀──▄███▀▄███──
──▐█▄▀█▄▀███─▄─▀─▄─███▀▄█▀▄█▌──
───███▄▀█▄██─██▄██─██▄█▀▄███───
────▀███▄▀██─█████─██▀▄███▀────
───█▄─▀█████─█████─█████▀─▄█───
───███────────███────────███───
───███▄────▄█─███─█▄────▄███───
───█████─▄███─███─███▄─█████───
───█████─████─███─████─█████───
───█████─████─███─████─█████───
───█████─████─███─████─█████───
───█████─████▄▄▄▄▄████─█████───
────▀███─█████████████─███▀────
──────▀█─███─▄▄▄▄▄─███─█▀──────
─────────▀█▌▐█████▌▐█▀─────────
────────────███████────────────
""")

    time.sleep(3)
    print("tank")
    time.sleep(2)
    print("""░░░░░░███████ ]▄▄▄▄▄▄▄▄
    ▂▄▅█████████▅▄▃▂
    I███████████████████].
    ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...
    """)

    time.sleep(3)
    print('bomb')

    time.sleep(2)
    print("""´´´´´´´´´´´´´´´´´´´´´´´$¶´´´´´¶´´´´´¶¢
    ´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¢´´´¶´´´ø¶
    ´´´´´´´´´´¶¶´´´´ø¶¶¶´´´´´´oø´´ø´´øo
    ´´´´´´´´´´¶7´´´´´´´¶¶¶´´´´´´1´´´1´´´´1o
    ´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶7´´´´´´´´1o¶¶¶ø
    ´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´1
    ´´´´´o¶¶¶¶¶¶¶¶¶ø´´´´´´´´´´´´´´´´´´o$¢
    ´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´¢´´1ø´´´1¶¶
    ´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶o´´´´´´´1$´´´¶
    ´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´¶´´´´o¶´
    ´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶
    ´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
    ´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
    ´´´´´¶¶¶¶¶¶¶¶¶¶¶¶´
    ´´´´´´´¶¶¶¶¶¶¶¶
    """)

    items = input("which item do you choose - the mech suit, tank or bomb : ")

    if (items == 'tank'):
        time.sleep(3)
        print('oh no the cyborg has ripped through the tank')
        time.sleep(3)
        print('you are running away to find safety')
        time.sleep(3)
        print('but the cyborg has seen you and captured you')

    elif (items == 'bomb'):
        time.sleep(3)
        print('you throw the bomb and it exlodes')
        time.sleep(3)
        print('but it doesnt even lay a scratch on him')
        time.sleep(3)
        print('because he is made from vibranium')
        time.sleep(3)
        print('you are instantly captured now')

    elif (items == "mech suit"):
        time.sleep(3)
        print('you are now in the mech suit')
        time.sleep(3)
        print('the cyborg is running towards you')
        time.sleep(3)
        print('this suit is highly advanced and gives you a ton of diffrent options')

        time.sleep(3)
        select_option = input("what would you like to use: rocket fist, missile, body slam: ")

        if (select_option == "rocket fist"):
            time.sleep(3)
            print('good the cyborg is extremely disorientated')
            time.sleep(3)
            combat_moves = input("do you want to throw a right hook or head butt: ")
            if (combat_moves == 'right hook'):
                time.sleep(3)
                print('wow your right hook to the cyborg was so DEVASTATING that it has killed him')
            elif (combat_moves == 'head butt'):
                time.sleep(3)
                print('incredible your head butt has KNOCKED OUT the cyborg')
        elif (select_option == 'missile'):
            time.sleep(3)
            print('oh no the cyborg is made from vibranium')
            time.sleep(3)
            print('the cyborg punches you and takes you back to the robots')
        elif (select_option == 'body slam'):
            time.sleep(3)
            print('the cyborg has been knocked unconsious good job')
            time.sleep(3)
            print('u have enough time to run')
# option to play again at completion of game
play_again = "yes"

while play_again == "yes" or play_again == "y":
    start()
    level1()
    path()
    again = choice()
    random_select(again)
    time.sleep(1)

    play_again = input("""Do you want to play again? 
    Type yes or y to play again and no or n if you want to stop: """)


stop_game = "no"
while stop_game == "no" or stop_game == "n":
        print('bye')
        break