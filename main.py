def initReactor(filename):
  reactions = []
  with open(filename, "r") as f:
    lines = [[l.strip(" ") for l in line.strip(" \n").split("=>")] for line in f.readlines()]

  for line in lines:
    costs = {}
    result = line[1].split(" ")
    costs[result[1]] = int(result[0])
    items = line[0].split(", ")
    for item in items:
      cost = item.split(" ")
      costs[cost[1]] = int(cost[0]) * -1
    reactions.append(costs)

  return reactions

def calcOre(reagents):
  unfinished = True
  while unfinished:
    unfinished = False

    #Scan the reagents list to see if we need anything and add it to the shopping list.
    toAdd = []
    for need in reagents.keys():
      if reagents[need] < 0 and need != "ORE":
        unfinished = True #If we have a non-ore need, loop again
        toAdd.append(need)

    #For each item in the shopping list
    for need in toAdd:
      for reaction in reactions:
        if need in reaction and reaction[need] > 0:
          for item in reaction.keys():
            if item in reagents:
              reagents[item] += reaction[item]
            else:
              reagents[item] = reaction[item]

  return reagents["ORE"] * -1

#HOLY SHIT INEFFICIENT
def calcFuel(reagents):
  fuelCount = 0
  while(reagents["ORE"] > 0):
    reagents["FUEL"] = -1
    calcOre(reagents)
    fuelCount += 1

  return fuelCount

#Part 1
fuel = {"FUEL" : -1}
#Part 2
ore = {"ORE": 1000000000000}
reactions = initReactor("reTest4")

print(calcOre(fuel))
print(calcFuel(ore))