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

def classCivQs():
  print("Classical World:")
  Question(1,"What year was Rome founded? ","753BC","753BCE")
  Question(2,"What the founder or Rome called? ","Romulus","Romulus")
  Question(3,"Who ordered the construction of the Colosseum? ","Vespasian","Emporer Vespasian")
  Question(4,"Who ordered the construction of the Great pyramid of Giza? ","Khufu","Pharaoh Khufu")
  Question(5,"What century was Troy defeated (format: xth C BC/AD? ","12th C BC","11th C BC")
  Question(6,"Who is the brother of Remus? ","Romulus","Romulus")
  Question(7,"What is the name of Alexander the Great's prominent city in Egypt? ","Alexandria","Alexandria")
  Question(8,"What is the prominent city state in Ancient Greece for warfare? ","Sparta","the spartans")
  Question(9,"Athens is named after which god/goddess? ","Athena","Athena")
  Question(10,"Where does Norse Mythology originate from? (region, not countries) ","Scandinavia","Nordic")
  print("You got a score of",Score,"!")
  roundcomplete = True


def mythQs():
  print("Classical Mythology:")
  Question(1,"What is the Greek form of Jupiter? ","Zeus","Zeus")
  Question(2,"Who is the king of the Greek gods? ","Zeus","Zeus")
  Question(3,"Who is the king of the Norse gods? ","Odin","allfather")
  Question(4,"Who is the king of the Greek Titans? ","Cronos","Kronos")
  Question(5,"Who is the king of the Egyptian gods ?(-on ending) ","Ammon","Amon")
  Question(6,"","","")
  Question(7,"","","")
  Question(8,"","","")
  Question(9,"","","")
  Question(10,"","","")
  print("You got a score of",Score,"!")
  roundcomplete = True
