import datetime
from pyttsx3 import engine
import speech_recognition as sr
import pyttsx3 as py
import winsound

engine = py.init()


def alarm(timing):
    alTime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))

    alTime = alTime[11:-3]
    print(alTime)
    Horeal = alTime[:2]
    Horeal = int(Horeal)
    Mireal = alTime[3:5]
    Mireal = int(Mireal)

    print(f"Done, alarm is set for {timing}")

    while True:
        if Horeal == datetime.datetime.now().hour and Mireal == \
                datetime.datetime.now().minute:
            print("alarm is running")
            winsound.PlaySound('abc', winsound.SND_LOOP)

        elif Mireal < datetime.datetime.now().minute:
            break


def speech(audio):
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print()
        print("Listening...")
        print()
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        print()
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        print()
        print(e)
        return "None"
    return query


speechinput = takeCommand().lower()

if 'alarm' in speechinput:
    speech("say set alarm for 5:30 am ")
    print("say set alarm for 5:30 am")
    tt = takeCommand()
    tt = tt.replace("set alarm to ", "")
    tt = tt.replace(".", "")
    tt = tt.upper()
    alarm(tt)
