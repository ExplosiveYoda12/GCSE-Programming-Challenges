#08 String Manipulation:
#Easy
favmovie = input("What is your favourite movie?: ")
favgame = input("What is your favourite game?: ")
favbook = input("What is your favourite book?: ")
favmoviefinal = favmovie[0:4].upper()
favgamefinal = favgame[0:2].lower()
favbookfinalfirst = favbook[0:1].upper()
favbookfinallast = favbook[1:4].lower()

string = favmoviefinal + favgamefinal + favbookfinalfirst + favbookfinallast
print(string)

#Medium
palindromeInput = input("Please enter a word to see if it is a palindrome: ")

if palindromeInput.upper() == palindromeInput.upper()[::-1]:
  print("Its a palindrome")
else:
  print("Not a palindrome")
