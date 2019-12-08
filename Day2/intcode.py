def initArray(filename):
  codes = open("Intcode.txt", "r")
  newArray = []

  for code in codes.read().split(","):
    newArray.append(int(code))
  
  codes.close()
  return newArray

def operateOn(array):
  nArr = array.copy()
  p = 0
  while True:

    if nArr[p] == 1:
      nArr[nArr[p+3]] = nArr[nArr[p+1]] + nArr[nArr[p+2]]
      p += 4

    elif nArr[p] == 2:
      nArr[nArr[p+3]] = nArr[nArr[p+1]] * nArr[nArr[p+2]]
      p += 4

    elif nArr[p] == 99:
      return nArr

    else:
      print("Unexpected OPCODE: " + str(nArr[p]))
      return -1

def checksum(value, filename):
  array = initArray(filename)
  for i in range(99):
    for j in range(99):
      tArray = array.copy()
      tArray[1] = i
      tArray[2] = j 
      tArray = operateOn(tArray)
      if tArray[0] == value:
        return 100 * i + j

  return -1

beforeArray = initArray("Intcode.txt")
afterArray = operateOn(beforeArray)

print(checksum(19690720, "Intcode.txt"))
print(afterArray[0])