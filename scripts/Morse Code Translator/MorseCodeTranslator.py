MORSE_CODES = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODES[letter] + " "
        else:
            cipher += " "
    return cipher


def decrypt(message):
    message += " "
    decipher = ""
    citext = ""  # stores morse code of a single character
    for letter in message:
        if letter != " ":
            i = 0  # keeps count of the spaces between morse characters
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += " "
            else:
                decipher += list(MORSE_CODES.keys())[
                    list(MORSE_CODES.values()).index(citext)
                ]
                citext = ""
    return decipher


def main():
    while True:
        print('''
            -----------------------------
            Morse Code Translator
            1. Encrypt
            2. Decrypt

            Enter 'q' to quit.
            -----------------------------
            ''')

        choice = input("Enter your choice: ")
        if choice == "1":
            message = input("Enter message to encrypt: ")
            result = encrypt(message.upper())
            print("> ", result)
        elif choice == "2":
            message = input("Enter message to decrypt: ")
            result = decrypt(message)
            print("> ", result)
        elif choice == "q":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
