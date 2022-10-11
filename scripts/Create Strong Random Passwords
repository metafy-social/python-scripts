# Generate Strong Random Passwords
import random
import string
# This script will generate an 18 character password
word_length = 18
# Generate a list of letters, digits, and some punctuation
components = [string.ascii_letters, string.digits, "!@#$%&"]
# flatten the components into a list of characters
chars = []
for clist in components:
  for item in clist:
    chars.append(item)
def generate_password():
  # Store the generated password
  password = []
  # Choose a random item from 'chars' and add it to 'password'
  for i in range(word_length):
    rchar = random.choice(chars)
    password.append(rchar)
  # Return the composed password as a string
  return "".join(password)
# Output generated password
print(generate_password())
