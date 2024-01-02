from getpass import getpass

guessCounter = int(1)
myNumber = int(getpass("Enter the secret number: "))

while True:  
  print("Guess Number")
  guess = int(input())

  
  if guess < myNumber:
    print("Too Low! Guess again.")
    guessCounter += 1
    continue
  elif guess > myNumber:
    print("Too High! Guess again.")
    guessCounter += 1
    continue
  elif guess == myNumber:
    print("You got it!")
    break
    guessCounter += 1
  else:
    print("Invalid Number")
    continue
    guessCounter += 1
  

print("It took you",guessCounter)