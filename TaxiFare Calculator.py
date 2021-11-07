def charge():
  distance = int(input("Distance in KM: "))
  if distance > 0:
      passengers = str(input("Passengers: "))
      cost = 2 * int(passengers)
      cost1 = 1.5 * int(distance)
      totalcost = int(cost) + int(cost1)
      print(totalcost)
  else:
      print("error")
      charge()
charge()
