import os, time

name = input("What is your name?\n").strip().capitalize()
age = input("What is your age?\n").strip()
phone = input("What is your phone?\n").strip()
email = input("What is your email?\n")
address = input("What is your address?\n")

myUser = {"name": name,  "age":age, "phone":phone, "email":email, "address":address}

os.system("clear")
time.sleep(1)

print(f"""🌟Contact Card🌟
  Hi {myUser['name']}.
Our dictionary says that you are {myUser['age']} years old.
We can call you on {myUser['phone']}, 
email you at{myUser['email']}, 
or send you mail at {myUser['address']}.""")