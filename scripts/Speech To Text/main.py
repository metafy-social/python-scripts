import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You've said : {}".format(text))
    except:
        print("Sorry can't understand... :(")
