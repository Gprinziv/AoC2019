#Day1 fuels.py
#Giovanni Prinzivalli
#05 December, 2019

import math

def recurFuel(mass):
  nextFuel = math.floor(int(mass)/3) - 2
  return recurFuel(nextFuel) + nextFuel if nextFuel > 0 else 0

def fuels(filename):
  fuel = 0
  modules = open(filename, "r")

  for module in modules:
    testFuel = recurFuel(int(module))
    fuel += testFuel
  
  modules.close()
  return fuel
  
def main():
  print(fuels("list.txt"))