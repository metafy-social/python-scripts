# pip install Faker
from faker import Faker

fake = Faker()

print("--------- Generate ---------------")
print("1. Name")
print("2. Email")
print("3. Job")
print("4. Address")

options = {1: fake.name(), 2: fake.email(), 3: fake.job(), 4: fake.address()}

print("----------------------------------")
user_input = int(input("Choose Option:- "))

print("----------------------------------")

if user_input in options:
    print(f"Result: {options[user_input]}")
else:
    print("Please try again with a valid option.")