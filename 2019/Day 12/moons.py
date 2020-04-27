import itertools
from functools import reduce
from math import gcd
import time

class Moon:
  def __init__(self, positions):
    self.vels = [0, 0, 0]
    self.pos = positions.copy()

  def calcEnergy(self):
    return sum(abs(i) for i in self.vels) * sum(abs(j) for j in self.pos)

  def updatePositions(self):
    for i in range(3):
      self.pos[i] += self.vels[i]

def initPositions(filename):
  positions = []
  with open(filename, "r") as f:
    for line in f.readlines():
      line = line.strip("<> \n")
      positions.append([int(val.strip(" zxy=")) for val in line.split(",")])
  return positions

def run(moons, steps):
  perms = list(itertools.combinations([i for i in range(len(moons))], 2))

  while steps > 0:
    for perm in perms:
      #Update the velocities of the moons at those two positions
      for i in range(3):
        if moons[perm[0]].pos[i] > moons[perm[1]].pos[i]:
          moons[perm[0]].vels[i] += -1
          moons[perm[1]].vels[i] += 1
        elif moons[perm[0]].pos[i] < moons[perm[1]].pos[i]:
          moons[perm[0]].vels[i] += 1
          moons[perm[1]].vels[i] += -1
    for moon in moons:
      moon.updatePositions()
    steps += -1

def findPeriod(moons, initPos):
  periods = dict()
  steps = 1

  while len(periods) < 3:
    run(moons, 1)
    steps += 1
    for i in range(3):
      if moons[0].pos[i] == initPos[0][i] and \
          moons[1].pos[i] == initPos[1][i] and \
          moons[2].pos[i] == initPos[2][i] and \
          moons[3].pos[i] == initPos[3][i] and \
          i not in periods:
        print(str(i) + ": " + str([moon.pos[i] for moon in moons]))
        print("Found period at step " + str(steps) + "!")
        periods[i] = steps

  return periods

def leaComMul(ps):
  return reduce(lambda a,b: (a * b) // gcd(a, b), ps)

"""
#Part 1
positions = initPositions("moons")
allMoons=[]
for pos in positions:
  allMoons.append(Moon(pos))
run(allMoons, 1000)
print(sum(moon.calcEnergy() for moon in allMoons))
"""

#Part 2
positions = initPositions("moons")
allMoons=[]
for pos in positions:
  allMoons.append(Moon(pos))

start_time = time.time()
print(positions)
periods = findPeriod(allMoons, positions)
print(leaComMul([p for p in periods.values()]))
print("--- %s seconds ---" % (time.time() - start_time))