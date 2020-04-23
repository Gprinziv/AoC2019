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

mapname = "astermap"
spaceMap = initMap(mapname)
best = findMax(spaceMap)

print("Best is at (" + str(best[0]) + "," + str(best[1]) + ") with count " + str(best[2]))