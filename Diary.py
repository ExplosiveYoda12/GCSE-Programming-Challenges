#MAIN FILE
import datetime

answer = input("read or write? ")
if answer.upper() == "READ":
  fi = open("diary.txt","r")
  print(fi.read())
  fi.close()
elif answer.upper() == "WRITE":
  f = open("diary.txt","a")
  text = input("Entry: ") 
  text2 = str(datetime.datetime.now())
  f.write("\n")
  f.write(text2)
  f.write("\n\n")
  f.write(text)
  f.write("\n\n\n")
  f.close()
  #+ SEPERATE FILE: 'diary.txt'
 
