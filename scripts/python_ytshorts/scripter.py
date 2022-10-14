# %%
from moviepy.editor import *
from IPython.display import Image
import pyttsx3
import wave
import contextlib
from random import randint
import requests
import spacy
import json

# %%
limit = 1
nlp=spacy.load("en_core_web_sm")
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)

def get_fact():
    response = requests.get(api_url, headers={'X-Api-Key': 'dY3dPGjWV0eJYJDe0s58fQ==h38UzNvlCb4SjqOO'})
    if response.status_code == requests.codes.ok:
        print(response.text)
        return response.text
    else:
        print("Error:", response.status_code, response.text)

flag=0
while(flag==0):
    fact= get_fact()
    # print(len(fact))
    doc=nlp(fact)
    # print (doc.ents)
    for X in doc.ents:
        #CAN ALSO DO IF X.label_=="GPE"
        if (len(fact)>=100):
            flag=1
            name=X.text
            break
print("\n"+name+"\n")
fact=json.loads(fact)[0]["fact"]
print(fact)




# %%
questiontext= "Did you know?"
answersay= fact

answertext= fact
answerlist=list(answertext)
i=30
while(i<len(answerlist)):
    if(answerlist[i]==" "):
        answerlist[i]="\n"
        if(i+30>=len(answerlist)):
            break
        i+=30
    else:
        i+=1

def convert(s):
    new = ""
    for x in s:
        new += x 
    return new
answertext= convert(answerlist)

# %%
engine = pyttsx3.init()
engine.save_to_file(answersay, 'static/test2.mp3' )
engine.runAndWait()

with contextlib.closing(wave.open("static/test2.mp3",'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    

# %%
knowaudio = AudioFileClip("static/test1.mp3")
knowaudioclip = CompositeAudioClip([knowaudio])
answeraudio = AudioFileClip("static/test2.mp3")
answeraudioclip = CompositeAudioClip([answeraudio])


# %%
x=randint(0,2)
y=randint(0,2)
z=randint(0,2)

def randomize_color(image):
    return image[:,:,[x,y,z]]

BackgroundClip= VideoFileClip("static/background.mp4").fl_image( randomize_color )



# %%
knowback= BackgroundClip.subclip(0,3) 
knowtext= TextClip(questiontext, fontsize=80, color="white" , font="Microsoft-Uighur-Bold", bg_color="black").set_position("center").set_duration(3)
knowclip= CompositeVideoClip([knowback,knowtext])
knowclip.audio= knowaudioclip

# %%
answerback= BackgroundClip.subclip(3,3+duration)
answertext= TextClip(answertext, fontsize=50, color="white" , font="Microsoft-Uighur", bg_color="black").set_position("center").set_duration(duration)
answerclip= CompositeVideoClip([answerback,answertext])
answerclip.audio= answeraudioclip

# %%
subscribeclip= VideoFileClip("static/Subscribe.mp4").fx(vfx.fadein, 1).fx(vfx.speedx, 2)

# %%
compile=concatenate_videoclips([knowclip, answerclip, subscribeclip], method="compose")
video = compile.resize(height=1920)
video = video.crop(x1=1166.6,y1=0,x2=2246.6,y2=1920)
video.save_frame("static/frame.png", 6)
Image(filename="static/frame.png")

# %%
video.write_videofile("static/temp.mp4", fps=60)

# %%
from test import *
upload(name.upper())

