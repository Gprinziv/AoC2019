def initNodes(filename):
  with open(filename, "r") as f:
    nodes = f.read().splitlines()

  return nodes

#The number of orbits a child makes is the number its parent makes, plus 1.
def findOrbits(nodes, parent, count):
  c = count

  for node in nodes:
    if parent == node.split(")")[0]:
      c += findOrbits(nodes, node.split(")")[1], count + 1)

  return c

def findPath(nodes, target, path):
  if target == "COM":
    path.append("COM")
  else:
    for node in nodes:
      if node.split(")")[1] == target:
        path.append(target)
        findPath(nodes, node.split(")")[0], path)
  return path

def orbTransfers(nodes, n1, n2):
  path1 = findPath(nodes, n1, [])
  path2 = findPath(nodes, n2, [])
  return len(set(path1) ^ set(path2)) - 2

nodes = initNodes("orbits")
print(orbTransfers(nodes, "YOU", "SAN"))
print(findOrbits(nodes, "COM", 0))