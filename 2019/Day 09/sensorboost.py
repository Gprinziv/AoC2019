import itertools

class Program:
  def __init__(self, filename, memSize = 1024):
    self.code = [0] * memSize
    with open(filename, "r") as f:
      for i, instr in enumerate(f.read().split(",")):
        self.code[i] = int(instr)

    self.p = 0
    self.relBase = 0
    self.inputs = []
    self.output = []

  def run(self):
    while self.p < len(self.code):
      self.p = performOp(self)
      if self.p < 0:
        return

def computeMode(code, addr, param, relBase):
  if param == 0:
    return code[addr]
  elif param == 1:
    return addr
  elif param == 2:
    return code[addr] + relBase
  else:
    print("Unexpected parameter. Operating in Position Mode.")
    return code[addr]

#Performs individual opertions.
#Returns a address of the next operation, or an error code if an operation fails.
def performOp(prog):
  #Just making the code less shit to write.
  code = prog.code
  p = prog.p
  relBase = prog.relBase
  #Divides an instruction into its components.
  opcode = code[p] % 100
  p1 = int(code[p] / 100) % 10
  p2 = int(code[p] / 1000) % 10
  p3 = int(code[p] / 10000)

  #OP 1: Addition. Add two parameters and write to location p3.
  if opcode == 1:
    para1 = computeMode(code, p+1, p1, relBase)
    para2 = computeMode(code, p+2, p2, relBase)
    para3 = computeMode(code, p+3, p3, relBase)
    code[para3] = code[para1] + code[para2]
    return p + 4

  #OP 1: Multiplication. Multiply two parameters and write to location p3.
  elif opcode == 2:
    para1 = computeMode(code, p+1, p1, relBase)
    para2 = computeMode(code, p+2, p2, relBase)
    para3 = computeMode(code, p+3, p3, relBase)
    code[para3] = code[para1] * code[para2]
    return p + 4

  #OP 3: Write. Input integer to location p1. Returns -3 if insufficient inputs.
  elif opcode == 3:
    para1 = computeMode(code, p+1, p1, relBase) 
    try:
      code[para1] = prog.inputs.pop()
    except IndexError:
      print("Insufficient number of inputs for program. Quitting.")
      return -3
    return p + 2
    
  #OP4: Read. Print value of location p1. Returns -4 if outputs invalid (not a list)
  elif opcode == 4:
    para1 = computeMode(code, p+1, p1, relBase)
    try:
      prog.output.append(code[para1])
    except IndexError:
      print("Failure to write to output")
      return -4
    return p + 2

  #OP5: Jump-if-true. If p+1 is nonzero, jump to p+2.
  elif opcode == 5:
    para1 = computeMode(code, p+1, p1, relBase)
    para2 = computeMode(code, p+2, p2, relBase)
    if code[para1] != 0:
      return code[para2]
    else:
      return p + 3

  #OP6: Jump-if-false: If p+1 is zerp, jump to p+2
  elif opcode == 6:
    para1 = computeMode(code, p+1, p1, relBase)
    para2 = computeMode(code, p+2, p2, relBase)
    if code[para1] == 0:
      return code[para2]
    else:
      return p + 3

  #OP7: Lesser. If p+1 is less than p+2, write 1 to p+3, else write 0.
  elif opcode == 7:
    para1 = computeMode(code, p+1, p1, relBase)
    para2 = computeMode(code, p+2, p2, relBase)
    para3 = computeMode(code, p+3, p3, relBase)
    code[para3] = 1 if code[para1] < code[para2] else 0
    return p + 4
      
  #OP8: Equals. If p+1 equals p+2, write 1 to p+3, else write 0.  
  elif opcode == 8:
    para1 = computeMode(code, p+1, p1, relBase)
    para2 = computeMode(code, p+2, p2, relBase)
    para3 = computeMode(code, p+3, p3, relBase)
    code[para3] = 1 if code[para1] == code[para2] else 0
    return p + 4

  #OP9: Relative Base Offset. Increments (or decrements) the relative base by the first parameter
  elif opcode == 9:
    para1 = computeMode(code, p+1, p1, relBase)
    prog.relBase += code[para1]
    return p + 2

  #OP99: Exit. Returns -1, indicating program completed siccessfully.
  elif code[p] == 99:
    return -1

  #Any other opcode. Returns -2, indicating a failure somewhere.
  else:
    print("ERROR: Unexpected OPCODE: " + str(code[p]))
    return -2

prog = Program("boost", 2048)
prog.inputs.append(2)
print("Running program")
prog.run()
print(prog.output)