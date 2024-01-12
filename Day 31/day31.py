def print_color(color):
  if color=="red":
    return ("\033[31m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")
  else:
    return ("\033[0m")

music_header = f"{print_color('red')}={print_color('white')}={print_color('blue')}={print_color('yellow')} Music App {print_color('blue')}={print_color('white')}={print_color('red')}="

print(f"      {music_header:^35}")
print(f"🔥▶️ \t{print_color('reset')}Radio Gaga")
print(f"{print_color('yellow')}\tQueen")
print(f"{print_color('white')}prev")
print(f"    {print_color('green')}next")
print(f"        {print_color('red')}pause")
print()
print()
welcome = "Welcome To"
armbook = "--  Armbook --"
line1 = "Definitely not a rip off"
line2 = "a certain other social"
line3 = "networking site"
honest = "Honest."
username = "Username:"
password = "Password:"
print(f"{print_color('reset')}{welcome:^35}")
print(f"{print_color('blue')}{armbook:^35}")
print(f"{print_color('yellow')}{line1:>35}")
print(f"{print_color('yellow')}{line2:>35}")
print(f"{print_color('yellow')}{line3:>35}")
print(f"{print_color('red')}{honest:^35}")
print(f"{print_color('reset')}{username:^35}")
print(f"{print_color('reset')}{password:^35}")