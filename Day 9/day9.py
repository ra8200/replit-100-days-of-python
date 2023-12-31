print("Learn what Generation you are!")
print()
age = int(input("What year were you born? "))
if 1925 <= age <= 1946 :
  print("You are part of the Tradionalists Generation.")
elif 1947 <= age <= 1964 :
  print("You are part of the Baby Boomer Generation.")
elif 1965 <= age <= 1981 :
  print("You are part of the Generation X Generation.")
elif 1982 <= age <= 1995 :
  print("You are part of the Millenials Generation.")
elif 1996 <= age <= 2015 :
  print("You are part of the Generation Z Generation.")
else:
  print("I have no idea")