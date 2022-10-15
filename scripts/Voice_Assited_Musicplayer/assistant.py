import pyttsx3
import speech_recognition as sr
import datetime
import os
from player import run

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

playlist = []


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def bot_answer(answer):
    print("assistant:", answer)


def greetings():
    global playlist
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("welcome to py-Musicplayer")
    bot_answer('say playlist name to play')
    playlist = os.listdir('Songs')
    bot_answer(playlist)


def action_taker():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("recognizing...")
        speak("recognizing")
        command = r.recognize_google(audio)
        print(f'User:{command}\n"')

    except Exception as e:
        print(e)
        bot_answer("Say that again please....")

        return "None"
    return command


greetings()
while True:
    command = action_taker().lower()
    song_playlist = list(map(str.lower, playlist))

    if any(command in s for s in song_playlist):
        get_ind = song_playlist.index(command)
        playlist_name = playlist.index(command)
        playlist_name = playlist[get_ind]
        playlist_dir = os.path.abspath("./Songs/"+playlist_name)
        bot_answer('Playing: '+playlist_name +
                   'playlist for you with Musicplayer')
        speak('playing:'+playlist_name+'playlist for you with music player')
        print(playlist_dir)
        run(playlist_dir)
    elif 'stop' in command:
        speak('good bye,have a good day')
        bot_answer('exit')
        engine.stop()
        break
    else:
        bot_answer('did not get the playlist...')
        speak('did not get the playlist')
        print(playlist)
