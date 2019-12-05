#Day2 intcode.py
#Giovanni Prinzivalli
#05 December, 2019

def initArray(filename):
  codes = open("Intcode.txt", "r")
  newArray = []

  for code in codes.read().split(","):
    newArray.append(int(code))
  
  codes.close()
  return newArray

def operateOn(array):
  p = 0
  while True:

    if array[p] == 1:
      print("OPCODE 1: Performing addition")
      print("Cell " + str(array[p+1]) + "; value: " + str(array[array[p+1]]))
      print("Cell " + str(array[p+2]) + "; value: " + str(array[array[p+2]]))
      print("Storing in location " + str(array[p+3]) + "\n")
      array[array[p+3]] = array[array[p+1]] + array[array[p+2]]
      p += 4

    elif array[p] == 2:
      print("OPCODE 2: Performing multiplication")
      print("Cell " + str(array[p+1]) + "; value: " + str(array[array[p+1]]))
      print("Cell " + str(array[p+2]) + "; value: " + str(array[array[p+2]]))
      print("Storing in location " + str(array[p+3]) + "\n")
      array[array[p+3]] = array[array[p+1]] * array[array[p+2]]
      p += 4

    elif array[p] == 99:
      print("Ending loop on OPCODE 99")
      return array

    else:
      print("Unexpected OPCODE: " + str(array[p]))
      return -1

beforeArray = initArray("Intcode.txt")
print(len(beforeArray))
print(beforeArray)
afterArray = operateOn(beforeArray)
print(afterArray[0])