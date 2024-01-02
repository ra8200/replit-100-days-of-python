while exit != "yes":
  animal = input("What animal do you want?: ")
  if animal == "Cow" or animal == "cow":
    print("A", animal, "goes Mooo")
  elif animal == "Dog" or animal == "dog":
    print("A", animal, "goes Bark")
  elif animal == "Cat" or animal == "cat":
    print("A", animal, "goes Meow")
  else:
    print("Yeah... I didn't programe that. ")
  exit = input("Do you want to exit?: ")