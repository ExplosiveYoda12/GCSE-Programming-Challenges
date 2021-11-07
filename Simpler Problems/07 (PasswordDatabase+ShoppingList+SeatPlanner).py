#07 Data Structures:
#Easy
on = True
to_do = []
def additem():
  item = input("Item")
  to_do.append(item)
def removeitem():
  item = input("Item to remove")
  to_do.remove(item)
def printlist():
  print (to_do)
while on:
  print ("1 = ADD ITEM")
  print ("2 = REMOVE ITEM")
  print ("3 = PRINT LIST")
  choice = int(input("CHOICE: "))
  if choice == 1:
    additem()
  elif choice == 2:
    removeitem()
  elif choice == 3:
    printlist()
  else:
    print ("INVALID CHOICE")

#Medium
on = True
login = {"Admin":"Test"}

def retPassword():
  passRet = input("What is the Username: ")
  try:
    print(login[passRet])
  except:
    print("Wrong Username")

def addUser():
  global username, password
  username = input("Username: ")
  password = input("Password: ")
  login[username] = password

while on:
  print ("\n1 = Add User")
  print ("2 = Retrieve Password")
  print ("3 = Exit and Clear Databse")
  choice = int(input("CHOICE: "))
  print("")
  if choice == 1:
    addUser()
  elif choice == 2:
    retPassword()
  elif choice == 3:
    login.clear()
    on = False
  else:
    print ("INVALID CHOICE")

#Hard
table = ["CHRIS", "DAVE", "SAM", "BOB", "SALLY"]

student = input("Who would you like to know the neighbours of in the seating plan? ").upper()

if student in table:
  indexpos = int(table.index(student))

  length = len(table) - 1
  endstudent = table[length]

  if student == endstudent:

    leftside = indexpos - 1
    lstudent = table[leftside]

    print("On the left of",student ,"is:", lstudent ,"and on the right is:", table[0])

  else:
    leftside = indexpos - 1
    rightside = indexpos + 1

    lstudent = table[leftside]
    rstudent = table[rightside]

    print("On the left of",student ,"is:",lstudent,"and on the right is:", rstudent)

else:
  print("Not in the seating plan")