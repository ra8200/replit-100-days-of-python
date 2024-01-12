toDoList = []

def printList():
  print() 
  for item in toDoList:
    print(item)
  print() 

while True:
  print("To DO list Manager:")
  menu = input("View, Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    toDoList.append(item)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print(f"{item} was not in the list")
  else:
    printList()

printList()
