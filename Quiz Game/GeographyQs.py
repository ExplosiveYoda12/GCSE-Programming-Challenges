from GlobalVariables import Score, roundcomplete

def Question(question_number,question,answer,answer2):
  global Score
  
  print("Question",question_number)
  q = input(question)
  if q.upper().strip() == answer.upper().strip() or q.upper().strip() == answer2.upper().strip():
    print("Correct\n")
    Score += 1
  else:
    print("Wrong\n")

def politicalGeoQs():
  print("Political Geography:")
  Question(1,"What is the Capital of Sweden? ","Stockholm","Stockholm")
  Question(2,"What is the Capital of Bangladesh? ","Dhaka","Dhaka")
  Question(3,"What is Cannberra the Capital of? ","Australia","Australia")
  Question(4,"What is the Capital of Finland? ","Helsinki","Helsinki")
  Question(5,"What is the Capital of Libya? ","Tripoli","Tripoli")
  Question(6,"What is New Delhi the Capital of? ","India","India")
  Question(7,"What is the Capital of Greece? ","Athens","Athens")
  Question(8,"What Country is Naxos part of? ","Greece","Greece")
  Question(9,"What Country is Gozo part of? ","Malta","Malta")
  Question(10,"What Country are the Falkland Islands part of? ","UK","United Kingdom")
  print("You got a score of",Score,"!")
  roundcomplete = True

def physicalGeoQs():
  print("Physical Geography:")
  Question(1,"What continent are the Ural Mountains in? ","Europe","Asia")
  Question(2,"What country is the ganges river in? ","India","Bangladesh")
  Question(3,"What is the ocean to the west of North America? ","Pacific","Pacific Ocean")
  Question(4,"What continent are the Atlas Mountains in? ","Africa","Africa")
  Question(5,"What is the largest island? ","Greenland","Greenland")
  Question(6,"What is the most heavily sought after sea to control? (trade) ","South China","South China Sea")
  Question(7,"What is the longest river in the world (dont type the word river in this answer)? ","Nile","The Nile")
  Question(8,"What is the widest river in the world?(dont type the word river in this answer) ","Amazon","The Amazon")
  Question(9,"What is the shallowest sea? ","Baltic","Baltic sea")
  Question(10,"Where is the deepest lake in the world(country/region)? ","Russia","Siberia")
  print("You got a score of",Score,"!")
  roundcomplete = True
