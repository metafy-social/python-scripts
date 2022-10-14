# Python script to get day-to-day horoscope
import os
import requests
import msvcrt
from bs4 import BeautifulSoup


def printBanner():
    banner = '''

    --------------------Read your Day-to-day horoscope------------------------
    ██╗  ██╗ ██████╗ ██████╗  ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗
    ██║  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
    ███████║██║   ██║██████╔╝██║   ██║███████╗██║     ██║   ██║██████╔╝█████╗  
    ██╔══██║██║   ██║██╔══██╗██║   ██║╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝  
    ██║  ██║╚██████╔╝██║  ██║╚██████╔╝███████║╚██████╗╚██████╔╝██║     ███████╗


    '''
    print(banner)


def read_horoscope(sign: int, day: int) -> str:
    if not isinstance(sign, int) or sign < 1 or sign > 12:
        return "Input a valid number the represents the sign from 1 to 12"
    if day < 1 or day > 3 or not isinstance(day, int):
        return "Input a valid number the represents the day from 1 to 3"
    days = ['yesterday', 'today', 'tomorrow']
    url = (
        f"https://www.horoscope.com/us/horoscopes/general/\
horoscope-general-daily-{days[day-1]}.aspx?sign={sign}"
        )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text


def refresh():
    os.system('cls')
    printBanner()


again = 'y'
while again == 'y':
    refresh()
    zodiac_sign = int(input(
        "Enter your Zodiac sign:\n\
[1] Aries\n[2] Taurus\n[3] Gemini\n[4] Cancer\n\
[5] Leo\n[6] Virgo\n[7] Libra\n[8] Scorpio\n\
[9] Sagittarius\n[10] Capricorn\n[11] Aquarius\n[12] Pisces\n> "
    ))
    refresh()
    print("Choose Day:\n[1] Yesterday\t[2] Today\t[3] Tomorrow:\n> ")
    day = int(str(msvcrt.getch())[2])
    refresh()
    print("Horoscope Reading\n---------------------------------------------\n")
    result = read_horoscope(zodiac_sign, day)
    print(result)
    print('\nDo you want to read horoscope again [y/n] > ')
    again = str(msvcrt.getch())[2].lower()
