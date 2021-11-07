#05 For Loops:
#Easy
num = int(input("Enter a number to get the times table of: "))
multiplier = int(input("Enter a number to get the length of this times table: "))
for i in range(multiplier):
  var = i * num
  print(i ,"x", num, "=", var)

#Medium
bottle = 99
for i in range (99,-1,-1):
  if bottle == 1:
    print(bottle,"bottles of beer on the wall.\n",bottle,"bottles of beer,\n",bottle,"bottles of beer, no more bottles on the wall.\n")
    print("no more bottles of beer on the wall, no more bottles of beer, go to the store and buy some more, 99 bottles of beer on the wall.\n")
    break
  else:
    print(bottle,"bottles of beer on the wall.\n",bottle,"bottles of beer,\n",bottle,"bottles of beer, take one down and pass it around.\n")
    bottle -= 1

#Hard
message = input("Hello, this program will remove the vowels from a message.\nPlease type in a message to change: ")

voweless = []
vowels = ["a","e","i","o","u"]
final_message = ""

for i in message:
  if i in vowels:
    pass
  else:
    voweless.append(i)

for i in voweless:
  final_message += i

print(final_message)
