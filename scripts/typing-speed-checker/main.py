from time import time

print("PARAGRAPH:")
print()

typingString = "Medical transcription, also known as MT, is an allied health profession dealing with the process of transcribing voice-recorded medical reports that are dictated by physicians, nurses and other healthcare practitioners. Medical reports can be voice files, notes taken during a lecture, or other spoken material."

words = len(typingString.split())

print(typingString)

print("\nAfter finishing the test, press the enter key to see your time and speed (in WPM)")
input("\nPress any key to Start:")

try:
    print("\nTimer Started\n")
    start = time()
    t = input()
    end = time()
    if t == typingString:
        total = round(end - start, 2)
        print("\nCongrats! You typed everything correctly.")
        print("You took was %s seconds" % total)
        total = int(total) / 60
        print("Your speed was %s wpm" % (str(words // total)))

    else:
        print("\nWrongly entered")
        print("Try again")

except KeyboardInterrupt:
    print("")