import os, time

website = {"name": None, "url": None, "desc": None, "rating": None}
for i in website.keys():
  website[i] = input(f"{i}: ")
os.system("clear")
time.sleep(1)
for i, j in website.items():
  print(f"{i}:{j}")