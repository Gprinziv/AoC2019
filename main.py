import itertools

#Needs a phase an an initial input value. 
class Amplifier:
  def __init__(self, phase):
    self.phase = phase

  def setInput(in1):
    self.in1 = in1

  def output():
    return self.output.pop()
    

#Takes a filename as input and returns a list object to be operated on
def initArray(filename):
  code = []
  with open(filename, "r") as f:
    for instr in f.read().split(","):
      code.append(int(instr))
  return code

#Operates on a program. Uses inputs from a list and outputs to a list.
def operateOn(code, inputs, outputs):
  p = 0
  while p < len(code):
    p = performOp(code, p, inputs, outputs)
    if p < 0:
      return p

  print("End of file reached without termination.")
  return -10

#Performs individual opertions.
#Returns a address of the next operation, or an error code if an operation fails.
def performOp(code, p, inputs, output):
  opcode = code[p] % 100
  p1 = int(code[p] / 100) % 10
  p2 = int(code[p] / 1000) % 10
  p3 = int(code[p] / 10000)

  #OP 1: Addition. Add two parameters and write to location p3.
  if opcode == 1:
    para1 = p+1 if p1 == 1 else code[p+1]
    para2 = p+2 if p2 == 1 else code[p+2]
    code[code[p+3]] = code[para1] + code[para2]
    return p + 4

  #OP 1: Multiplication. Multiply two parameters and write to location p3.
  elif opcode == 2:
    para1 = p+1 if p1 == 1 else code[p+1]
    para2 = p+2 if p2 == 1 else code[p+2]
    code[code[p+3]] = code[para1] * code[para2]
    return p + 4

  #OP 3: Write. Input integer to location p1. Returns -3 if insufficient inputs.
  elif opcode == 3: 
    try:
      code[code[p+1]] = inputs.pop()
    except IndexError:
      print("Insufficient number of inputs for program. Quitting.")
      return -3
    return p + 2
    
  #OP4: Read. Print value of location p1. Returns -4 if outputs invalid (not a list)
  elif opcode == 4:
    para1 = p+1 if p1 == 1 else code[p+1]
    try:
      output.append(code[para1])
    except IndexError:
      print("Failure to write to output")
      return -4
    return p + 2

  #OP5: Jump-if-true. If p+1 is nonzero, jump to p+2.
  elif opcode == 5:
    para1 = p+1 if p1 == 1 else code[p+1]
    para2 = p+2 if p2 == 1 else code[p+2]
    if code[para1] != 0:
      return code[para2]
    else:
      return p + 3

  #OP6: Jump-if-false: If p+1 is zerp, jump to p+2
  elif opcode == 6:
    para1 = p+1 if p1 == 1 else code[p+1]
    para2 = p+2 if p2 == 1 else code[p+2]
    if code[para1] == 0:
      return code[para2]
    else:
      return p + 3

  #OP7: Lesser. If p+1 is less than p+2, write 1 to p+3, else write 0.
  elif opcode == 7:
    para1 = p+1 if p1 == 1 else code[p+1]
    para2 = p+2 if p2 == 1 else code[p+2]
    code[code[p+3]] = 1 if code[para1] < code[para2] else 0
    return p + 4
      
  #OP8: Equals. If p+1 equals p+2, write 1 to p+3, else write 0.  
  elif opcode == 8:
    para1 = p+1 if p1 == 1 else code[p+1]
    para2 = p+2 if p2 == 1 else code[p+2]
    code[code[p+3]] = 1 if code[para1] == code[para2] else 0
    return p + 4

  #OP99: Exit. Returns -1, indicating program completed siccessfully.
  elif code[p] == 99:
    return -1

  #Any other opcode. Returns -2, indicating a failure somewhere.
  else:
    print("ERROR: Unexpected OPCODE: " + str(code[p]))
    return -2

def checksum(value, filename):
  array = initArray(filename)
  for i in range(99):
    for j in range(99):
      tArray = array.copy()
      tArray[1] = i
      tArray[2] = j 
      tArray = operateOn(tArray, 1)
      if tArray[0] == value:
        return 100 * i + j

  return -1

""" Part 1
phases = [0, 1, 2, 3, 4]
perms = list(itertools.permutations(phases))
outputs = []
ampfile = "ampcontrol"

for code in perms:
  ampA = operateOn(initArray(ampfile), [0, code[0]], outputs)
  ampB = operateOn(initArray(ampfile), [outputs.pop(), code[1]], outputs)
  ampC = operateOn(initArray(ampfile), [outputs.pop(), code[2]], outputs)
  ampD = operateOn(initArray(ampfile), [outputs.pop(), code[3]], outputs)
  ampE = operateOn(initArray(ampfile), [outputs.pop(), code[4]], outputs)

print(max(i for i in outputs))
"""

phases = [5, 6, 7, 8, 9]
perms = list(itertools.permutations(phases))
outputs = []
ampfile = "ampcontrol"

for code in perms:
  return "Fuck"