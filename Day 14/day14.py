from getpass import getpass

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1 = getpass("Player 1 > ")
player2 = getpass("Player 2 > ")

if player1=="R" or player1=="r":
  if player2=="R" or player2=="r":
    print("Tie")
  elif player2=="P" or player2=="p":
    print("Player 2 wins")
  elif player2=="S" or player2=="s":
    print("Player 1 wins")
  else:
    print("Invalid move")
elif player1=="S" or player1=="s":
  if player2=="r" or player2=="r":
    print("Player 2 wins")
  elif player2=="P" or player2=="p":
    print("Player 1 wins")
  elif player2=="S" or player2=="s":
    print("Tie")
  else:
    print("Invalid move")
elif player1=="P" or player1=="p":
  if player2=="R" or player2=="r":
    print("Player 1 wins")
  elif player2=="P" or player2=="p":
    print("Tie")
  elif player2=="S" or player2=="s":
    print("Player 1 wins")
  else:
    print("Invalid move")
else:
  print("Invalid move")