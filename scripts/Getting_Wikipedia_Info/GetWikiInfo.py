import wikipedia
import pyttsx3 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
query = input("What You Want To Ask ??")
results = wikipedia.summary(query, sentences=2)
speak("According to Wikipedia\n")
print(results)
speak(results)