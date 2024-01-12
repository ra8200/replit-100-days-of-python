import os, time
toDoList = ['work', 'sleep', 'eat', 'code']

def printList():
  os.system("clear")
  print()
  counter = 1
  for item in toDoList:
    print(f"{counter}: {item}")
    counter +=1
  print()
  time.sleep(1)

while True:
  print("To-Do list Manager:")
  menu = input("1. Add to To-Do List\n2: Remove from To-Do List\n3. Show To-Do List\n>")
  if menu == "1":
    item = input("What's next on the Agenda?: ")
    if item in toDoList:
      print(f"'{item}' is already on the list!")
    else:
      toDoList.append(item)
  elif menu == "2":
    item = input("What do you want to remove?: ")
    if item in toDoList:
      areYouSure = input("Are you sure? yes or no\n")
      if areYouSure == 'yes' or areYouSure == 'Yes':
        toDoList.remove(item)
    else:
      print(f"{item} was not in the list")
  else:
    printList()

printList()