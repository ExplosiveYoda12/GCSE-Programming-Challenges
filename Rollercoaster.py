height = int(input("What is your height in cm?"))
numOfRiders = 0

while numOfRiders != 8:
  if height >= 140:
    print("You can ride alone")
    numOfRiders += 1
    height = int(input("What is your height in cm?"))
  elif height < 120:
    print("You can't ride")
    height = int(input("What is your height in cm?"))
  elif height <= 120 and height >= 139:
    adult = input("Are you riding with an adult?(Y/N)")
    if adult.upper() == "Y":
      print("You can ride with an adult")
      numOfRiders += 2
      height = int(input("What is your height in cm?"))
    else:
      print("You can't ride")
      height = int(input("What is your height in cm?"))
  else:
    height = int(input("What is your height in cm?"))

print("Ride goes")
