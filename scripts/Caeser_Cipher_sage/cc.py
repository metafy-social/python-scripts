# @author https://github.com/theadeyemiolayinka

from statistics import mode


class Caesar():

    def __init__(self):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''

    def __crypt(self, mode):
        for symbol in self.message.upper():
            if symbol in self.LETTERS:
                num = self.LETTERS.find(symbol)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(self.LETTERS):
                    num = num - len(self.LETTERS)
                elif num < 0:
                    num = num + len(self.LETTERS)

                self.translated = self.translated + self.LETTERS[num]
            else:
                self.translated = self.translated + symbol

        return self.translated

    def encrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('encrypt')

    def decrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('decrypt')

def invokeCipher(cipher, key, text, e_mode):
    if e_mode == 'E' or e_mode == 'e':
        print('\n====================RESULT====================')
        return cipher.encrypt(text, key)
    elif e_mode == 'D' or e_mode == 'd':
        print('\n====================RESULT====================')
        return cipher.decrypt(text, key)
    else:
        print('Ivalid mode.')
        n_mode = str(input("Enter mode: [E] for encryption and [D] for decryption:\n>"))
        return invokeCipher(cipher, key, text, n_mode)
    
cipher = Caesar()
key = int(input('Enter encryption key:\n>'))
text = str(input('Enter text:\n>'))
e_mode = str(input("Enter mode: [E] for encryption and [D] for decryption:\n>"))

print(invokeCipher(cipher, key, text, e_mode))
print('==============================================')
