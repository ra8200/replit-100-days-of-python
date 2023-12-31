print("--Enter your username and password--")
print()
username = input("Username: > ")
password = input("Password: > ")
print()
if username == "rob" and password == "password1":
  print("Welcome Rob.")
elif username == "mike" and password == "password2":
  print("Welcome Mike.")
elif username == "jim" and password == "password3":
  print("Welcome Jim.")
elif username == "kyle" and password == "password4":
  print("Kyle is a douchy name.")
else: 
  print("Wrong Username and/or password. Please try again.")