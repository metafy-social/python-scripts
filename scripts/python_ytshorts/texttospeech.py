import pyttsx3

questiontext= "Did you know?"
answertext= "Australia is wider than the moon. The moon sits at 3400km in diameter, while Australia’s diameter from east to west is almost 4000km."

engine = pyttsx3.init()
engine.save_to_file(questiontext, 'test1.mp3')
engine.save_to_file(answertext, 'test2.mp3' )
engine.runAndWait()
