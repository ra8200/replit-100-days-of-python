def print_color(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color == "purple":
    print("\033[35m", word, sep="", end=",")
  elif color == "green":
    print("\033[32m", word, sep="", end=", ")
  else: 
    print("\033[0m", word, sep="", end="")


print("Super Function?")
print("coloring text using a FUNCTION")
print_color("red","Words and more words ")
print_color("reset","line change ")
print_color("green", "means go ")
print_color("reset", "line change ")
print_color("purple" , "another sentence")
