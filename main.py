def initMap(filename):
  with open(filename, "r") as f:
    spaceMap = f.read().splitlines()
  return spaceMap

def computeMap(spaceMap):
  maxAsteroids = 0
  return maxAsteroids

mapname = "astTest1"
spaceMap = initMap(mapname)
maxAsteroids = computeMap(spaceMap)
print(spaceMap)
for line in spaceMap:
  print(line) 


#Figure out how many asteroids (any character not a '-') each asteroid on the map can see (not including self).
  #Start at the origin of the asteroid, calculate distance 1, then distance 2, then distance 3, etc. Backcheck to see if the angle of vision matches an already detected asteroid. If yes, move on, if no, count++.
#Update map with the number visible as you go. 
#return the index of the max number



"""
for each '#' in space:
  make an asteroid object with coords at map location and an empty array
for asteroid in space:
  for asteroidsAfter in space:
    Calculate angle to each other on the map and if it's unique, preserve it in both asteroids.
  Count the number of angles stored in the list, and return the max.
  """