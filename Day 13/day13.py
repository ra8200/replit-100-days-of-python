print("What is the name of your test? ")
test = input()
print("What is the maximum score you can get on this test? ")
maxScore = int(input())
print("What was your score? ")
userScore = float(input())
print()

numberScore = float(userScore / maxScore)
finalScore = round(numberScore, 2)
percentage = (userScore / maxScore) * 100

print("Name of exam: ", test)
print()
print("Max. Possible Score: ", maxScore)
print()
print("Your Score: ", userScore)
print()
print("You got", percentage,"%")

if finalScore >= .90:
  print("You got an A!")
elif finalScore >= .80 and finalScore <= .89:
  print("You got a B!")
elif finalScore >= .70 and finalScore <= .79:
  print("You got a C!")
elif finalScore >= .60 and finalScore <= .69:
  print("You got a D!")
else:
  print("You got an F!")