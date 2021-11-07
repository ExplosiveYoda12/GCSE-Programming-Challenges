active = True
packages = []

while active == True:
  pack = int(input("\nEnter the weight for the item. 0 to quit: "))
  if pack == 0:
    active = False
  elif pack < 0:
    print("Error. No negatives allowed\n")
  else:
    packages.append(pack)

packages.sort()
numOfPackages = len(packages)
lightestPackage = packages.index[0] #error
heaviestPackage = packages.index[len-1]
print("There are",numOfPackages,"packages. The lightest weighs",lightestPackage,"and the heaviest weighs",heaviestPackage,)
