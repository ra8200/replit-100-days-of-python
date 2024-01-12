from getpass import getpass
users = "david"
answer= "baldies4life"

def login():
  while True:
    username = input("What is your username?:")
    password = getpass("What is your password?:")
    print()
    if username == users and password == answer:
      print("Welcome back", users)
      break
    else:
      print("Wrong username or password. Try again")
      continue
      
print("Login System")
login()