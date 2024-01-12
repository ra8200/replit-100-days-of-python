print("30 Days Down - Thoughts?")
print()

for i in range(1, 31):
  thoughts = input(f"Day {i}:\n")
  print()
  response = f"You thought Day {i} was"
  print(f"{response:^30}")
  print(f"{thoughts:^30}")
  print()