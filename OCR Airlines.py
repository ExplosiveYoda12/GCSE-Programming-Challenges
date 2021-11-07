passengerLuggage = float(input("How much Luggage do you have in kg? "))
cost = 0

if passengerLuggage <= 25.0:
  print("You have under or equal to 25kg, no extra charge")
elif passengerLuggage >= 50.0:
  print("You have too much luggage")
else:
  passLug = round(passengerLuggage - 25.0)
  while passLug != 0.0:
    cost += 10.0
    passLug -= 1.0
  print("You will be charged £",cost,"for your extra luggage") 
