def checksum(num):
    result = 0
    for digit in range(0, len(str(num))):
        result += int(str(num)[digit])
    return result


print("Input your Credit Card Number you want to validate:")
input = str(input())

if len(input) < 12 or len(input) > 16:
    print("The number is too short or too long")
    exit()

checkDigit = input[-1]
number = input[:-1]
sumOfNumbers = 0

for digit in range(0, len(number)):
    current = int(number[len(number) - digit - 1])
    if digit % 2 == 0:
        current *= 2
    sumOfNumbers += checksum(current)

sumOfNumbers *= 9

if str(sumOfNumbers)[-1] == checkDigit:
    print("Number is likely valid")
else:
    print("Number is likely invalid")
