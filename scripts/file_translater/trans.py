# Imports
import googletrans
from googletrans import *


translator = googletrans.Translator()

f1 = input("Enter source file (with .txt extension)")
f2 = open(f1, encoding="utf8")
data = f2.read()
# print(data)
f3 = input("Enter destination file (with .txt extension)")
f4 = open(f3, encoding="utf8", mode="w")
f2.close()

# input_text = input('Input Your Translation Text : ')
input_language = input('Input Your Translation Language : ')

translation = translator.translate(data, dest=input_language)
print(translation.text)
f4.write(translation.text)
f4.close()
