year = input("Is this a leap year?: ")
regular = 60 * 60 * 24 * 365
leap = 60 * 60 * 24 * 366

if year == "yes" or year == "Yes":
  print(leap)
elif year == "no" or year == "No":
  print(regular)
else:
  print("Wrong answer")