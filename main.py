import math

def initMap(filename):
  with open(filename, "r") as f:
    spaceMap = f.read().splitlines()
  return spaceMap

def printMap(spaceMap):
  for line in spaceMap:
    print(line)

def calcVisible(sMap, astX, astY):
  count = 0
  angles = []
  for y in range(len(sMap)):
    for x in range(len(sMap[y])):
      if astX == x and astY == y:
        pass
      elif sMap[y][x] == '#':
        angle = math.atan2(y - astY, x - astX)
        if angle not in angles:
          count += 1
          angles.append(angle)

  return count

def findMax(spaceMap):
  maxAst = 0
  maxX = -1
  maxY = -1

  for y in range(len(spaceMap)):
    for x in range(len(spaceMap[y])):
      if spaceMap[y][x] == '#':
        count = calcVisible(spaceMap, x, y)
        if count > maxAst:
          maxX = x
          maxY = y
          maxAst = count

  return [maxX, maxY, maxAst]

def vaporizeUntil(sMap, n):
  popped = 0
  #Find the laser coordinates. 
  #Calculate the angle in radians of every single asteroid and sort it first by angle, then by distance.
  #pop a value, set a reminder to the current angle, and then pop the next one that has a different angle than the reminder.
  #repeat this process until you get the n you want
  return x, y, popped

mapname = "astermap"
spaceMap = initMap(mapname)

#part1
x, y, count = findMax(spaceMap)
print("Best is at (" + str(x) + "," + str(y) + ") with count " + str(count))
spaceMap[y] = spaceMap[y][:x] + "X" + spaceMap[y][x + 1:]

val = vaporizeUntil(spaceMap, 200)
print(val)