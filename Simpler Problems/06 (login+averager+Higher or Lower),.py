#06 While Loops:
#Easy
import time
active = True
username = "ADMIN"
password = "TEST"

def login():
  time.sleep(1)
  print("\nAuthenticating...")
  for i in range(0,3):
    print("\n.....")
    time.sleep(1)
  print("\nACCEPTED\nWelcome",username,"\n")


while active == True:
  usernameInput = input("USERNAME>>> ")
  if usernameInput.upper() == username:
    passwordInput = input("PASSWORD>>> ")
    if passwordInput.upper() == password:
      login()
      active = False
    else:
      print("Password Rejected\n")
  else:
    print("Username Rejected\n")

#Medium
import statistics

average_num = 0
active = True
amountToAverage = 0
aves = []

while active == True:
  score = input("Please enter a result to average: ")
  if score.upper() == "EXIT":
    active = False
    average = sum(aves) / len(aves)
    print(average)
    print("Average Score:",average)
  else:
    aves.append(int(score))
    amountToAverage += 1

#Hard
import random

computer_number =random.randint( 1 , 100 )

def is_same( target , number ):
    if target == number:
        result = "Win"
    elif target > number:
        result = "Low"
    else:
        result = "High"
    return result

print("Hello.\nI have thought of a number between 1 and 100.")

guess = int(input("Can you guess it?\n\n"))

higher_or_lower = is_same(computer_number, guess)

while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess = int(input("Sorry, you are too low. Try again. "))
    else:
        guess = int(input("Sorry, you are too high. Try again "))

    higher_or_lower = is_same(computer_number, guess)

input("Correct!\nWell Done\n\n\nPress RETURN to exit.")
