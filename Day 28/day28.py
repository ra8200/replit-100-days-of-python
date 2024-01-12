import os, time, random

def dice(sides):
  result = random.randint(1, sides)
  return result

def strength_stat():
  strength = ( ( dice(6) * dice(12) ) / 2 ) + 12
  return strength

def health_stat():
  health = ( ( dice(6) * dice(12) ) / 2 ) + 10
  return health

# Character 1
name1 = ["Trevor the Douche", "Sally the Great", "Dragon Slayer Kelly"]
race1 = ["Human", "Elf", "Dwarf"]
random_name1 = random.choice(name1)
random_race1 = random.choice(race1)
print("D&D Hero Generator ⚔️")
print()
print("Character Name: ", random_name1)
print("Character Race: ", random_race1)
strength1 = strength_stat()
health1 = health_stat()
print("Strength: ", strength1)
print("Health: ", health1)
print()
print("March forth to Glory", random_name1, "!")
print()

# Character 2
name2 = ["Johnny Boy", "Sir Mix-A-Lot", "Trisha, The King's Bane"]
race2 = ["Troll", "Orc", "Goblin"]
random_name2 = random.choice(name2)
random_race2 = random.choice(race2)
print("D&D Hero Generator ⚔️")
print()
print("Character Name: ", random_name2)
print("Character Race: ", random_race2)
strength2 = strength_stat()
health2 = health_stat()
print("Strength: ", strength2)
print("Health: ", health2)
print()
print("March forth to Glory", random_name2, "!")
print()

# Game
round = 1
winner = None

while True:
  time.sleep(5)
  os.system("clear")
  print(" ⚔️ Lets Fight! ⚔️ ")
  print()
  
  hero1 = dice(6)
  hero2 = dice(6)

  power_diff = abs(strength1 - strength2) + 1

  if hero1 > hero2:
    health2 -= power_diff
    if round == 1:
      print(random_name1, "Wins!")
    else:
      print(random_name1, "wins round", round)
  elif hero2 > hero1:
    health1 -= power_diff
    if round == 1:
      print(random_name2, "Wins!")
    else:
      print(random_name2, "wins round", round)
  else:
    print("Draw,", round)

  print()
  print(random_name1)
  print("Health:", health1)
  print()
  print(random_name2)
  print("Health:", health2)
  print()

  if health1 <= 0:
    print(random_name1, "has died!")
    winner = random_name2
    break
  elif health2 <= 0:
    print(random_name2, "has died!")
    winner = random_name1
    break
  else:
    print("They both are standing for the for next round!")
    round += 1

time.sleep(3)
os.system("clear")
print(winner, "Is The Champion!")
print()
print(winner, "has won in", round, "rounds")
