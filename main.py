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

minZeroes = layerList[0].count('0')
indexOfMin = 0
for i, layer in enumerate(layerList):
  zeroCount = layer.count('0')
  if zeroCount < minZeroes:
    minZeroes = zeroCount
    indexOfMin = i

print(minZeroes)
print(layerList[indexOfMin].count('2') * layerList[indexOfMin].count('1'))