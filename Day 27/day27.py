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

while True:
  names = ["Johnny Boy", "Trevor the Douche", "Sir Mix-A-Lot", "Sally the Great", "Trisha, The King's Bane", "Dragon Slayer Kelly"]
  races = ["human", "troll", "elf", "dwarf", "gnome", "orc", "goblin"]
  random_name = random.choice(names)
  random_race = random.choice(races)
  print("D&D Hero Generator ⚔️")
  print()
  print("Character Name: ", random_name)
  print("Character Race: ", random_race)
  print("Strength: ", strength_stat())
  print("Health: ", health_stat())
  print()
  print("March forth to Glory", random_name, "!")
  print()
  new_hero = input("Want to create another hero? (yes or no) \n")
  if new_hero == "No" or new_hero == "no":
    break
  time.sleep(2)
  os.system("clear")