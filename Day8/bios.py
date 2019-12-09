class Layer:
  def w(): return 25
  def h(): return 6

#Read thru the file and make layers
def makeLayers(filename):
  layerSize = Layer.w() * Layer.h()
  layers = []

  with open(filename, "r") as f:
    allLayers = f.read()
    while allLayers:
      layers.append(allLayers[:layerSize])
      allLayers = allLayers[layerSize:]

  return layers

layerList = makeLayers("layers")

#Part 1
minZeroes = layerList[0].count('0')
indexOfMin = 0
for i, layer in enumerate(layerList):
  zeroCount = layer.count('0')
  if zeroCount < minZeroes:
    minZeroes = zeroCount
    indexOfMin = i

print(layerList[indexOfMin].count('2') * layerList[indexOfMin].count('1'))

layerList.reverse()
password = [0 for i in range(Layer.h() * Layer.w())]

for layer in layerList:
  for i, val in enumerate(layer):
    if int(val) < 2:
      password[i] = val

for i in range(Layer.h()):
  print("".join(password)[i * Layer.w() : (i + 1) * Layer.w()].replace('0', ' ').replace('1', 'X')) 