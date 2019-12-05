#open the file. Returns any number of wires to be plotted as a list.
def initWires(filename):
  with open(filename, "r") as f:
    wires = list(line.replace("\n", "") for line in f.readlines())
  return wires

#Plot a given wire. Returns a list of tuples corresponding to the positions of the line
def plotWire(wire):
  pos = [0,0]
  
  for instr in wire.split(","):
    for i in range(int(instr[1:])):
      pos[0 if (instr[0] == 'L' or instr[0] == 'R') else 1] += -1 if (instr[0] == 'L' or instr[0] == 'D') else 1
      yield tuple(pos)

#Find the intersect of the wires. Returns the shortest distance.
def shortManDist(wire1, wire2):
  intersects = set(wire1) & set(wire2)
  return min(abs(x) + abs(y) for (x, y) in intersects)

wires = initWires("wires.txt")
wire1 = plotWire(wires[0])
wire2 = plotWire(wires[1])
print(shortManDist(wire1, wire2))

wires = initWires("wireTest1")
wire1 = plotWire(wires[0])
wire2 = plotWire(wires[1])
print(shortManDist(wire1, wire2))

wires = initWires("wireTest2")
wire1 = plotWire(wires[0])
wire2 = plotWire(wires[1])
print(shortManDist(wire1, wire2))
