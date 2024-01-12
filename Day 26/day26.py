from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False
  while True:
    play_stop= int(input("Press 2 to stop the song : "))
    if play_stop == 2:
      source.paused = True
      return
    else:
      continue
    
while True:
  os.system("clear")
  print("🎵 My Musak")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Stop")
  time.sleep(1)
  user_choice = int(input())
  if user_choice == 1:
    play()
  elif user_choice == 2:
    exit()
  else:
    continue