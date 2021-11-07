#MAIN FILE
enteringTeams = open("enteredTeams.txt","r")
cupTeams = open("cupTeams.txt","a")

for line in enteringTeams:
  country = enteringTeams.readline()
  name = input("Who would you like to assign to a Team? ")
  cupTeams.write("\n")
  cupTeams.write(country)
  cupTeams.write(name)
  cupTeams.write("\n\n")

enteringTeams.close()
cupTeams.close()

#SEPERATE FILE 'enteredTeams.txt'

England 

France 

Germany 

Ireland 

Spain 
#SEPERATE EMPTY FILE 'cupTeams.txt'
