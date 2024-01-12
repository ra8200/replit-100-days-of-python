print("Pick a number between 1 and 20!")
print("Crazy, i know")
print()
print("I will tell you how many tries it took you to guess the number.")
print()

import random
guessCounter = 1
randomNum = random.randint(1,20)

while True:
  print("Pick a number between 1 and 20.")
  userNum = int(input())
  if userNum < randomNum:
    print("lower")
    guessCounter += 1
  elif userNum > randomNum: 
    print("higher")
    guessCounter += 1
    continue
  elif userNum == randomNum:
    print("wow, u did it...")
    break
    exit()
  else: 
    print("i dont know how you did this. die")
print("It took you", guessCounter, "trys to guess the number.")