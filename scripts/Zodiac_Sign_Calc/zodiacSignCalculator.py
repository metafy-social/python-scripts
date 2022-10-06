##Takes in the month as the input
month = int(input("Enter the month number that you were born: "))

##if the month is valid the x is true. where x is a flag
if(month>0 and month <12):
    print()
    x=True
else:
    print("wrong month, pls restart the program")
    x=False

##if the flag is true then it checks the month and the date and prints the zodiac sign
if(x):
    day = int(input("Enter the day you were born:"))
    
    if month==3:
        sign = "Pisces" if(day < 21) else "Aries"
    elif month==4:
        sign = "Aries" if(day < 20) else "Tourus"
    elif month==5:
        sign = "Tourus" if(day < 21) else "Gemini"
    elif month==6:
        sign = "Gemini" if(day < 21) else "Cancer"
    elif month==7:
        sign = "Cancer" if(day < 23) else "Leo"
    elif month==8:
        sign = "Leo" if(day < 23) else "Virgo"
    elif month==9:
        sign = "Virgo" if(day < 23) else "Libra"
    elif month==10:
        sign = "Libra" if(day < 23) else "Scorpio"
    elif month==11:
        sign = "Scorpio" if(day < 22) else "Sagittarius"
    elif month==12:
        sign = "Sagittarius" if(day < 22) else "Capricorn"
    elif month==1:
        sign = "Capricorn" if(day < 20) else "Aquarius"
    elif month==2:
        sign == "Aquarius" if(day < 19) else "Pisces"

    print()
    print("Your zodiac sign is "+sign)
