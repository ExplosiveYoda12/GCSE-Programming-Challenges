#NOT COMPLETE BUT USABLE

import GeographyQs
import ClassCivMythQs
import GeneralQs
from GlobalVariables import Score, roundcomplete


name = input("What is your name? ")
print("\nHello",name, "Welcome to Quizmaster!\n\nThere are 5 categories to choose from:\nPolitical Geography(1)\nPhysical Geography(2)\nClassical World(3)\nClassical Mythology (Grk + Rmn)(4)\nGeneral Questions(5)\n")

def quizchoice():
  quizSection = input("Type the number for the section you wish to start with: ")
  print("")
  if quizSection == "1":
    GeographyQs.politicalGeoQs()
  elif quizSection == "2":
    GeographyQs.physicalGeoQs()
  elif quizSection == "3":
    ClassCivMythQs.classCivQs()
  elif quizSection == "4":
    ClassCivMythQs.mythQs()
  elif quizSection == "5":
    GeneralQs.generalQs()
  else:
    print("Error, try again")
    quizchoice()

quizchoice()
if roundcomplete == True:
  print("Well Done, You may choose a new section\n")
  quizchoice()
  roundcomplete = False
else:
  print("Thank you for playing!\nYour final Score was",Score,"!")
