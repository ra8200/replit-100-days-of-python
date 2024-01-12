import random

def dice(sides):
  result = random.randint(1, sides)
  return result

def strength_stats():
  five = dice(5)
  six = dice(6)
  strength = five * six
  return strength
  
def dexterity_stats():
  five = dice(5)
  six = dice(6)
  dexterity = five * six
  return dexterity
  
def constitution_stats():
  five = dice(5)
  six = dice(6)
  constitution = five * six
  return constitution
  
def intelligence_stats():
  five = dice(5)
  six = dice(6)
  intelligence = five * six
  return intelligence
  
def wisdom_stats():
  five = dice(5)
  six = dice(6)
  wisdom = five * six
  return wisdom
  
def charisma_stats():
  five = dice(5)
  six = dice(6)
  charisma = five * six
  return charisma

print("D&D Stat Generator ⚔️")
print()

new_hero = "yes"

while new_hero == "yes":
  Hero = input("What is your hero's name: ")
  print()
  strength = str(strength_stats())
  dexterity = str(dexterity_stats())
  constitution = str(constitution_stats())
  intelligence = str(intelligence_stats())
  wisdom = str(wisdom_stats())
  charisma = str(charisma_stats())
  print("Your hero's Strength is", strength)
  print()
  print("Your hero's Dexterity is", dexterity)
  print()
  print("Your hero's Constitution is", constitution)
  print()
  print("Your hero's Intelligence is", intelligence)
  print()
  print("Your hero's Wisdom is", wisdom)
  print()
  print("Your hero's Charisma is", charisma)
  print()
  print("Want to create another hero? (yes or no)")
  new_hero = input()
