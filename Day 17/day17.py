# from getpass import getpass

# player1Score = 0
# player2Score = 0

# print("E P I C    🪨  📄 ✂️    B A T T L E ")
# print("Best out of 3")
# print()

# while True:
#   print()
#   print("Select your move (R, P or S)")
#   print()

#   player1 = getpass("Player 1: ")
#   player2 = getpass("Player 2: ")

#   if player1=="R" or player1=="r":
#     if player2=="R" or player2=="r":
#       print("Tie")
#     elif player2=="P" or player2=="p":
#       print("Player 2 wins the round")
#       player2Score += 1
#     elif player2=="S" or player2=="s":
#       print("Player 1 wins the round")
#       player1Score += 1
#     else:
#       print("Invalid move")
#       continue
#   elif player1=="S" or player1=="s":
#     if player2=="r" or player2=="r":
#       print("Player 2 wins the round")
#       player2Score += 1
#     elif player2=="P" or player2=="p":
#       print("Player 1 wins the round")
#       player1Score += 1
#     elif player2=="S" or player2=="s":
#       print("Tie")
#     else:
#       print("Invalid move")
#       continue
#   elif player1=="P" or player1=="p":
#     if player2=="R" or player2=="r":
#       print("Player 1 wins the round")
#       player1Score += 1
#     elif player2=="P" or player2=="p":
#       print("Tie")
#     elif player2=="S" or player2=="s":
#       print("Player 2 wins the round")
#       player2Score += 1
#     else:
#       print("Invalid move")
#       continue
#   else:
#     print("Invalid move")
#     continue
    
#   if player1Score == 3 or player2Score == 3:
#     break

# if player1Score > player2Score:
#   print("Player 1 is the winner!")
# else: 
#   print("Player 2 is the winner!")

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")