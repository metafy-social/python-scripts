# create random password of given length
import string
import random
def create_password(length):
    temp_password = ''
    for i in range(length):
        temp_password += random.choice(string.ascii_letters+ string.digits+'!@#$%^&*()')
    return password
length=int(input("Enter length of password: "))
print(create_password(length))