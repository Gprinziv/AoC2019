#intersects.py
#by Giovanni Prinzivalli
#05 December, 2019

#open the file. Returns two wires to be plotted.
def initWires(filename):
 with open(filename, "r") as f:
  print(wire) for wire in f.readlines()
return wires

#Plot both wires. Returns a list of tuples corresponding to the positions of the line
def plotWire(wire):
  pos = [0,0]
  #Traverse the path of the wire
  for instr in wire.split(","):
    #go the direction a number of times
    yield tuple(pos)

#Find the intersect of the wires. Returns the shortest distance.
def shortManDist(wire1, wire2):
  intersects = set(wire1) & set(wire2)
  return min(abs(x) + abs(y) for (x, y) in intersects)

wires = initWires("wires.txt")
test1 = initWires(wireTest1)
test2 = initWires(wireTest2)

print(wires)
print(test1)
print(test2)