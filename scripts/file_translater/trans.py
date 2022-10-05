import googletrans
from googletrans import *

translator = googletrans.Translator()

f1 = input("Enter source file (with .txt extension)")

data = None

# f2 is the file object which reads the source file
with open(f1, encoding="utf8") as f2:
  data = f2.read()
  
f3 = input("Enter destination file (with .txt extension)")

# f4 is the file object which writes to the output file
with open(f3, encoding="utf8", mode="w") as f4:

  input_language = input('Input Your Translation Language : ')

  translation = translator.translate(data, dest=input_language)
  print(translation.text)
  f4.write(translation.text)
