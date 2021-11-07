from GlobalVariables import Score, roundcomplete
#kept Question func in each file as kept running into circular import errors
def Question(question_number,question,answer,answer2):
  global Score
  
  print("Question",question_number)
  q = input(question)
  if q.upper().strip() == answer.upper().strip() or q.upper().strip() == answer2.upper().strip():
    print("Correct\n")
    Score += 1
  else:
    print("Wrong\n")

def generalQs():
  print("General Questions:")
  Question(1,"","","")
  Question(2,"","","")
  Question(3,"","","")
  Question(4,"","","")
  Question(5,"","","")
  Question(6,"","","")
  Question(7,"","","")
  Question(8,"","","")
  Question(9,"","","")
  Question(10,"","","")
  print("You got a score of",Score,"!")
  roundcomplete = True
