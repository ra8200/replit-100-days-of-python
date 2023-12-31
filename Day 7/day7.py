anime = input("What's your anime?\n").lower()
if anime == "demon slayer":
  print("Hell yeah!, mee too.")
  demonSlayer = input("Who's your favorite character?").lower()
  if demonSlayer == "tanjiro":
    print("He is too nice but a perfect MC.")
  elif demonSlayer == "inosuke":
    print("Its weird how he figurs everything out first.")
  elif demonSlayer == "zenitsu":
    print ("""You can argue he may be the strongest, 
           but not the most annoying.""")
  elif demonSlayer == "nezuko":
    print("She is amazing.")
  else: 
    print("Thats Cool, I like them too.")
elif anime == "attack on titan":
  print("That show was intense.")
  aotCharacter = input("Levi or Mikasa?").lower()
  if aotCharacter == "mikasa":
    print("She's a bad ass.")
  elif aotCharacter == "levi":
    print("He's my favorite.")
  else:
    print("Wrong answer")
else:
  print("Oh cool, I like that too.")
