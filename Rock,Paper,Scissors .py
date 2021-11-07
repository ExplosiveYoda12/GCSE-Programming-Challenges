import random

def init():
  print("Hello, Welcome to rock paper scissors")

def choice():
  global rpsPlayer
  print("Rock\nPaper\nScissors")
  playerChoice = input("Choice: ")
  if playerChoice.upper() == "PAPER":
    rpsPlayer = "paper"
    pass
  elif playerChoice.upper() == "ROCK":
    rpsPlayer = "rock"
    pass
  elif playerChoice.upper() == "SCISSORS":
    rpsPlayer = "scissors"
    pass
  else:
    print("Invalid Input please try again")
    choice()

def computerNum():
  global rpsComputer
  compNum = random.randint(1,3)
  if compNum == 1:
    rpsComputer = "paper"
  elif compNum == 2:
    rpsComputer = "rock"
  elif compNum == 3:
    rpsComputer = "scissors"
  else:
    computerNum()

def calculateWin(rpsPlayer, rpsComputer):
  if rpsPlayer == rpsComputer:
    print("Draw,",rpsPlayer,"draws with",rpsComputer)
  elif rpsPlayer != rpsComputer:

    if rpsPlayer == "rock" and rpsComputer == "paper":
      print("Lose,",rpsPlayer,"loses to",rpsComputer)
    elif rpsPlayer == "rock" and rpsComputer == "scissors":
      print("Win,",rpsPlayer,"beats",rpsComputer)

    elif rpsPlayer == "paper" and rpsComputer == "rock":
      print("Win,",rpsPlayer,"beats",rpsComputer)
    elif rpsPlayer == "paper" and rpsComputer == "scissors":
      print("Lose,",rpsPlayer,"loses to",rpsComputer)

    elif rpsPlayer == "scissors" and rpsComputer == "rock":
      print("Lose,",rpsPlayer,"loses to",rpsComputer)
    elif rpsPlayer == "scissors" and rpsComputer == "paper":
      print("Win,",rpsPlayer,"beats",rpsComputer)

  else:
    print("error")


init()
choice()
computerNum()
calculateWin(rpsPlayer, rpsComputer)
