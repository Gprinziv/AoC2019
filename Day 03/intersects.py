#Open the file. 
#Inputs filename with raw wire data.
#Returns any number of wires to be plotted as a list.
def initWires(filename):
  with open(filename, "r") as f:
    wires = list(line.replace("\n", "") for line in f.readlines())

  return wires

#Plot a given wire. 
#Inputs a "wire" string as a series of comma separated instructions
#Returns a list of tuples corresponding to the positions of the line
def plotWire(wire):
  pos = [0,0]
  
  for instr in wire.split(","):
    for i in range(int(instr[1:])):
      pos[0 if (instr[0] == 'L' or instr[0] == 'R') else 1] += -1 if (instr[0] == 'L' or instr[0] == 'D') else 1
      yield tuple(pos)

#Find the intersect of the wires. 
#inputs two lists of wire data.
#Returns the shortest distance.
def shortManDist(wire1, wire2):
  return min(abs(x) + abs(y) for (x, y) in set(wire1) & set(wire2))

#Find the closest intersect to the origin.
#Inputs two lists of wire data.
#Returns the number of steps to the closest intersection.
def shortSteps(wire1, wire2):
  return min(2 + wire1.index(i) + wire2.index(i) for i in list(set(wire1) & set(wire2)))

wires = initWires("wires.txt")
wire1 = list(plotWire(wires[0]))
wire2 = list(plotWire(wires[1]))
print(shortManDist(wire1, wire2))
print(shortSteps(wire1, wire2))