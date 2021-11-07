#01 Basics:
#Easy
name = input("What is your name? ")
print("Hello",name)

#Medium
name = input("What is your name? ")
print       ("Hello",name,)
age = input("How old are you? ")
print("Thats good",name,"that you are ", age)
favoritefilm = input("What is your favorite film? ")
favoritebook = input("What is your favorite book? ")
print(name, "is" ,age, "and likes" ,favoritefilm, "and" ,favoritebook)

#Hard
print("Please enter some measurements to work out the dimensions of a rectangle.")
width = int(input("Please input a width: "))
height = int(input("Please input a height: "))
area = width * height
print("\nThe area of the rectangle is:",area)
#--------------------------------------------------
#02 Data Types:
#Easy
num = float(input("Enter a number: "))
answer = num / 2
print(answer)

#Medium
name = input("Hello, what is your name? ")
age = int(input("How old are you? "))
ageold = 50
agetotal = (age + ageold)
print ("Nice to meet you",name,",you are",age,"years old!")
print ("In 50 years you will be",agetotal)

#Hard
name = input("What is your name? ")
print("Please enter some measurements to work out the volume of a cuboid.")
width = int(input("Please input a width: "))
height = int(input("Please input a height: "))
depth = int(input("Please input a depth: "))
volume = width * height * depth
print("\nHello",name,"The volume of the cuboid is:",volume)
#--------------------------------------------------
#03 Operators:
#Easy
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
div = num1 / num2
mul = num1 * num2
add = num1 + num2
sub = num1 - num2
mod = num1 % num2
fdiv = num1 // num2
print("Division:",div,"Multiplication:",mul,"Addition:",add,"Subtraction:",sub,"Modulus:",mod,"Floor Division:",fdiv)

#Medium
name = input("Hello, What is your name? ")
age = input("How old are you? ")
age = int(age)
nameage = name * age
print(nameage)

#Hard
sleep = int(input("How many hours of sleep per night do you have? "))
week = sleep * 7
month = week * 4.345
year1 = month * 12
year = year1 / 24

print("\nIn a week you sleep",week,"hours")
print("\nIn a month you sleep",int(month),"hours")
print("\nIn a year you sleep",int(year1),"hours")
print("\nIn a year you sleep",int(year),"days")
