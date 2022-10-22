import random
b=input("Do you want to roll the dice?y/n: ")
if b=='y':
  a=int(input("Number of times you want to roll: "))
  print("Result: ")
  for i in range(0,a):
    ans=random.randint(1,6)
    print(i+1,".",ans)
else:
  print("Good Bye!")