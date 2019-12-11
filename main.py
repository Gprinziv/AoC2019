import itertools

class Intcode:
  #initializes code from a "punchcard" with a default of 1024 memory locations.
  def __init__(self, filename, memSize = 1024):
    self.code = [0] * memSize
    with open(filename, "r") as f:
      for i, instr in enumerate(f.read().split(",")):
        self.code[i] = int(instr)

    self.p = 0
    self.relBase = 0
    self.inputs = []
    self.output = []

  #Runs the program from start to finish.
  #Optional parameters:
    #inputVal: A single (for now) input value to be used when running the program
    #numOuts: The program runs until the number of outputs is reached, then pauses.
  def run(self, inputVal = None, numOuts = None):
    if inputVal is not None:
      self.inputs.append(inputVal)

    while 0 <= self.p < len(self.code):
      self.p = performOp(self)
      if numOuts is not None and len(self.output) == numOuts:
        return

  #Computes the mode of parameters being passed into an operation. Returns the proper address for the code to execute from.
  def computeMode(self, offset):
    param = int(self.code[self.p] / (pow(10, offset + 1))) % 10
    
    if param == 0:
      return self.code[self.p + offset]
    elif param == 1:
      return self.p + offset
    elif param == 2:
      return self.code[self.p + offset] + self.relBase
    else:
      print("Unexpected parameter. Operating in Position Mode.")
      return self.code[self.p + offset]

class Robot:
  def __init__(self, w = 100, h = 50):
    self.grid = [[0 for i in range(w)] for j in range(h)] #I'm clearly fucking this up.
    self.x = int(w/2)
    self.y = int(h/2)
    self.facing = 0

  #Rotate clockwise if rotate is 1, counterclockwise if rotate is 0
  #Facing: 0 - Up, 1 - Right, 2 - Down, 3 - Left
  def changeFace(self, rotate):
    #Ensures that turning counterclockwise leaves you facing left
    self.facing = (self.facing + 4 + (1 if rotate == 1 else -1)) % 4
  

  #moves forward 1 step based on facing.
  def move(self):
    if self.facing == 0:
      self.y += -1
    elif self.facing == 1:
      self.x += 1
    elif self.facing == 2:
      self.y += 1
    else:
      self.x += -1

  def paint(self, color):
      self.grid[self.y][self.x] = color if color == 1 else 2

  def getColor(self):
    return 1 if self.grid[self.y][self.x] == 1 else 0

def paintShip():
  prog = Intcode("paintcode", 2048)
  rob = Robot()

  rob.paint(1)
  newInput = rob.getColor()
  while True:
    prog.run(newInput, 2)
    if(prog.p < 0):
      print("Finish with code " + str(prog.p))
      break
    rob.changeFace(prog.output.pop())
    rob.paint(prog.output.pop())
    rob.move()
    newInput = rob.getColor()

  #OH MY GOD i HAVE A HEADACHE. I can't figure out how to better print this.
  listOfStrings = []
  for line in rob.grid:
    listOfStrings.append(''.join([str(elem) for elem in line]))
  for line in listOfStrings:
    print(line.replace('0', ' ').replace('1', 'X').replace('2', ' '))

#Performs individual opertaions.
#Returns a address of the next operation, or an error code if an operation fails.
#Must eventually work into Program class, I think.
def performOp(prog):
  #Just making the code less shit to write.
  code = prog.code
  p = prog.p
  relBase = prog.relBase
  opcode = code[p] % 100

  #OP 1: Addition. Add two parameters and write to location p3.
  if opcode == 1:
    para1 = prog.computeMode(1)
    para2 = prog.computeMode(2)
    para3 = prog.computeMode(3)
    code[para3] = code[para1] + code[para2]
    return p + 4

  #OP 1: Multiplication. Multiply two parameters and write to location p3.
  elif opcode == 2:
    para1 = prog.computeMode(1)
    para2 = prog.computeMode(2)
    para3 = prog.computeMode(3)
    code[para3] = code[para1] * code[para2]
    return p + 4

  #OP 3: Write. Input integer to location p1. Returns -3 if insufficient inputs.
  elif opcode == 3:
    para1 = prog.computeMode(1)
    try:
      code[para1] = prog.inputs.pop()
    except IndexError:
      print("Insufficient number of inputs for program. Quitting.")
      return -3
    return p + 2
    
  #OP4: Read. Print value of location p1. Returns -4 if outputs invalid (not a list)
  elif opcode == 4:
    para1 = prog.computeMode(1)
    try:
      prog.output.append(code[para1])
    except IndexError:
      print("Failure to write to output")
      return -4
    return p + 2

  #OP5: Jump-if-true. If p+1 is nonzero, jump to p+2.
  elif opcode == 5:
    para1 = prog.computeMode(1)
    para2 = prog.computeMode(2)
    if code[para1] != 0:
      return code[para2]
    else:
      return p + 3

  #OP6: Jump-if-false: If p+1 is zerp, jump to p+2
  elif opcode == 6:
    para1 = prog.computeMode(1)
    para2 = prog.computeMode(2)
    if code[para1] == 0:
      return code[para2]
    else:
      return p + 3

  #OP7: Lesser. If p+1 is less than p+2, write 1 to p+3, else write 0.
  elif opcode == 7:
    para1 = prog.computeMode(1)
    para2 = prog.computeMode(2)
    para3 = prog.computeMode(3)
    code[para3] = 1 if code[para1] < code[para2] else 0
    return p + 4
      
  #OP8: Equals. If p+1 equals p+2, write 1 to p+3, else write 0.  
  elif opcode == 8:
    para1 = prog.computeMode(1)
    para2 = prog.computeMode(2)
    para3 = prog.computeMode(3)
    code[para3] = 1 if code[para1] == code[para2] else 0
    return p + 4

  #OP9: Relative Base Offset. Increments (or decrements) the relative base by the first parameter
  elif opcode == 9:
    para1 = prog.computeMode(1)
    prog.relBase += code[para1]
    return p + 2

  #OP99: Exit. Returns -1, indicating program completed siccessfully.
  elif code[p] == 99:
    return -1

  #Any other opcode. Returns -2, indicating a failure somewhere.
  else:
    print("ERROR: Unexpected OPCODE: " + str(code[p]))
    return -2


paintShip()

#Most basic program executable.
#Expected output: 82760.
#Ensures I didn't mess something up royally.
prog = Intcode("boost", 2048)
print("Running boost program...")
prog.run(2)
print(prog.output)