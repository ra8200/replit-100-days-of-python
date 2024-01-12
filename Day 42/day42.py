import os, time

fakemon = {"Name": None, "Element": None, "Special Move": None, "HP": None, "MP": None}
print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()

for i in fakemon.keys():
  fakemon[i] = input(f"What is your Fakemon's {i}?\n").strip().title()

if fakemon["Element"]=="earth":
  print("\033[32m", end="")
elif fakemon["Element"]=="air":
  print("\033[37m", end="")
elif fakemon["Element"]=="fire":
  print("\033[31m", end="")
elif fakemon["Element"]=="water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

os.system("clear")
time.sleep(1)

for i, j in fakemon.items():
  print(f"{i:<10}: {j}")
