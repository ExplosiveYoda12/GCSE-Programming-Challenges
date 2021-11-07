#04 If Statements:
#Easy
age = int(input("How old are you? "))
if age == 17:
  print("You can drive a car")
elif age > 10 and age < 17:
  print("You can be criminally responsible")
elif age >= 18:
  print("You can drink, or drive")
else:
  print("Other")

#Medium
score = 0
name = input("Hello, What is your name? ")

Q1 = input("What is the largest Island in the Planet? ")
if Q1.upper() == "GREENLAND":
  print("Correct")
  score += 1
else:
  print("Wrong")

Q2 = input("What is the largest Continent? ")
if Q2.upper() == "ASIA":
  print("Correct")
  score += 1
else:
  print("Wrong")

Q3 = input("What is the largest Country? ")
if Q3.upper() == "RUSSIA":
  print("Correct")
  score += 1
else:
  print("Wrong")

Q4 = input("What is the smallest Country? ")
if Q4.upper() == "VATICAN CITY":
  print("Correct")
  score += 1
else:
  print("Wrong")

Q5 = input("What is the largest Inland sea? ")
if Q5.upper() == "CASPIAN SEA":
  print("Correct")
  score += 1
else:
  print("Wrong")

print("Hello",name,"you got a score of:",score)

#Hard
score = 0
name = input("What is your name? ")
print("Hello",name, "Welcome to my Geography Quiz")
print("There are ten questions, Good Luck!")

print("\nQuestion 1")
q1 = input("What is the Capital of Sweden ")
if q1 == "Stockholm":
    print('Correct')
    score += 1

    print("Question 2")
    q2 = input("What is the Capital of Bangladesh? ")
    if q2 == "Dhaka":
        print("Correct")
        score += 1

        print("Question 3")
        q3 = input("What is Canberra the Capital of? ")
        if q3 == "Australia":
            print("Correct")
            score += 1

            print("Question 4")
            q4 = input("What is the Capital of Finland? ")
            if q4 == "Helsinki":
                print("Correct")
                score += 1

                print("Question 5")
                q5 = input("What is the Capital of Libya? ")
                if q5 == "Tripoli":
                    print("Correct")
                    score += 1

                    print("Question 6")
                    q6 = input("What is New Delhi the Capital of? ")
                    if q6 == "India":
                        print("Correct")
                        score += 1

                        print("Question 7")
                        q7 = input("What is the Capital of Greece? ")
                        if q7 == "Athens":
                            print("Correct")
                            score += 1

                            print("Question 8")
                            q8 = input("What Country is Naxos part of? ")
                            if q8 == "Greece":
                                print("Correct")
                                score += 1

                                print("Question 9")
                                q9 = input("What Country is Gozo part of? ")
                                if q9 == "Malta":
                                    print("Correct")
                                    score += 1

                                    print("Question 10")
                                    q10 = input("What Country is the Falkland Islands part of?  ")
                                    if q10 == "United Kingdom":
                                        print("Correct ")
                                        score += 1
else:
  print("Wrong")

print("You got",score,"out of 10")
if score < 5:
    print("Better luck next time!")
if score > 5:
    print("Well done!")
if score == 5:
    print("Eh....")
