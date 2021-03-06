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

def vaporizeUntil(sMap, lasX, lasY, n):
  asteroids = []
  for y in range(len(sMap)):
    for x in range(len(sMap[y])):
      if sMap[y][x] == "#":
        dist = math.sqrt((y - lasY) ** 2 + (x - lasX) ** 2)
        angle = math.degrees(math.atan2(y - lasY, x - lasX))
        angle = (angle + 90) if angle >= -90 else (angle + 450)
        asteroids.append([angle, dist, 100 * x + y])
  asts = sorted(asteroids)
  for line in asts:
      print(line)


  while n > 0:
    lastAngle = -1
    itr = 0
    while itr < len(asts) and n > 0:
      if asts[itr][0] == lastAngle:
        itr += 1
      else:
        last = asts.pop(itr)
        print("Vaporizing #" + str(201-n) + " at location " + str(last[2]))
        lastAngle = last[0]
        n -= 1

  return last[2]

mapname = "astermap"
spaceMap = initMap(mapname)

#part1
x, y, count = findMax(spaceMap)
print("Best is at (" + str(x) + "," + str(y) + ") with count " + str(count))
spaceMap[y] = spaceMap[y][:x] + "X" + spaceMap[y][x + 1:]

#part2
val = vaporizeUntil(spaceMap, x, y, 200)
print(val)