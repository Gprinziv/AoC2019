import math

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

def calcOre(fuel = 1):
  reagents = {"FUEL": -1 * fuel}

  unfinished = True
  while unfinished:
    unfinished = False

    #Scan the reagents list to see if we need anything and add it to the shopping list.
    toAdd = []
    for need in reagents.keys():
      if reagents[need] < 0 and need != "ORE":
        unfinished = True #If we have a non-ore need, loop again
        toAdd.append(need)

    #For eac reagent we need
    for need in toAdd:          
      for reaction in reactions: #Check the list of reactions and find a match
        if need in reaction and reaction[need] > 0: #Find the right expression
          numTimes = math.ceil(abs(reagents[need]) / reaction[need])
          for item in reaction.keys():
            if item in reagents:
              reagents[item] += reaction[item] * numTimes
            else:
              reagents[item] = reaction[item] * numTimes
                
  return reagents["ORE"] * -1

reactions = initReactor("reactions")
#Part 1
ore = calcOre() #Ore per unit of fuel
print("Part 1 answer: " +  str(ore))

#Part 2
limit = 10 ** 12 #Our goal
minimum = math.ceil(limit / ore) #The minimum amount of fuel we'll need
answer = calcOre(minimum) #How much that actually gets us
maximum = int(minimum * (limit / answer) ** 2)

while minimum < maximum:
  mid = (minimum + maximum) // 2
  answer = calcOre(mid)
  if answer < limit:
    minimum = mid + 1
  elif answer > limit:
    maximum = mid - 1
  else:
    break
while answer > limit:
  mid += -1
  answer = calcOre(mid)
print(mid)