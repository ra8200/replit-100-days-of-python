print("Fill in the blank lyrics!")
print()
print("Type in the missing lyric that goes in the blank and see if you are cool or not!")
print()

counter = 1
while True:
  lyric = input("Never going to ______ you up.")
  if lyric == "give" or lyric == "Give":
    print("You got it!")
  else:
    print("Nope, Try again")
    counter += 1
  if lyric == "give" or lyric == "Give":
    break
print("Thanks for playing!")
print()
print("You got the correct lyrics in", counter, "attempt(s).")