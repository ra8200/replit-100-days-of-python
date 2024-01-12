my_list = []

def print_list():
  print()
  counter = 1
  for name in my_list:
    print(f"{counter}: {name}")
    counter +=1
  print()


while True:
  print("Names of Peoples")
  first_name = input("What is your first name?\n").strip().capitalize()
  last_name = input("What is your last Name?\n").strip().capitalize()
  name = (f"{first_name} {last_name}")
  if name in my_list:
    print("You fucked up")
  else:
    my_list.append(name)
  print_list()