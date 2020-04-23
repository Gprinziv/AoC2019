from collections import deque

class Intcode:
  #initializes code from a "punchcard" with a default of 1024 memory locations.
  def __init__(self, filename, memSize = 4096):
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
      if self.inputs != []:
        self.inputs.pop()
      self.inputs.append(inputVal)

    while 0 <= self.p < len(self.code):
      self.p = self.performOp()
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

  #Performs individual opertaions.
  #Returns a address of the next operation, or an error code if an operation fails.
  def performOp(self):
    code = self.code
    p = self.p
    opcode = code[p] % 100

    #OP 1: Addition. Add two parameters and write to location p3.
    if opcode == 1:
      para1 = self.computeMode(1)
      para2 = self.computeMode(2)
      para3 = self.computeMode(3)
      code[para3] = code[para1] + code[para2]
      return p + 4

    #OP 1: Multiplication. Multiply two parameters and write to location p3.
    elif opcode == 2:
      para1 = self.computeMode(1)
      para2 = self.computeMode(2)
      para3 = self.computeMode(3)
      code[para3] = code[para1] * code[para2]
      return p + 4

    #OP 3: Write. Input integer to location p1. Returns -3 if insufficient inputs.
    elif opcode == 3:
      para1 = self.computeMode(1)
      try:
        code[para1] = self.inputs.pop()
      except IndexError:
        code[para1] = 0
        #print("Insufficient number of inputs for program. Quitting.")
        #return -3
      return p + 2
      
    #OP4: Read. Print value of location p1. Returns -4 if outputs invalid (not a list)
    elif opcode == 4:
      para1 = self.computeMode(1)
      try:
        self.output.append(code[para1])
      except IndexError:
        print("Failure to write to output")
        return -4
      return p + 2

    #OP5: Jump-if-true. If p+1 is nonzero, jump to p+2.
    elif opcode == 5:
      para1 = self.computeMode(1)
      para2 = self.computeMode(2)
      if code[para1] != 0:
        return code[para2]
      else:
        return p + 3

    #OP6: Jump-if-false: If p+1 is zerp, jump to p+2
    elif opcode == 6:
      para1 = self.computeMode(1)
      para2 = self.computeMode(2)
      if code[para1] == 0:
        return code[para2]
      else:
        return p + 3

    #OP7: Lesser. If p+1 is less than p+2, write 1 to p+3, else write 0.
    elif opcode == 7:
      para1 = self.computeMode(1)
      para2 = self.computeMode(2)
      para3 = self.computeMode(3)
      code[para3] = 1 if code[para1] < code[para2] else 0
      return p + 4
        
    #OP8: Equals. If p+1 equals p+2, write 1 to p+3, else write 0.  
    elif opcode == 8:
      para1 = self.computeMode(1)
      para2 = self.computeMode(2)
      para3 = self.computeMode(3)
      code[para3] = 1 if code[para1] == code[para2] else 0
      return p + 4

    #OP9: Relative Base Offset. Increments (or decrements) the relative base by the first parameter
    elif opcode == 9:
      para1 = self.computeMode(1)
      self.relBase += code[para1]
      return p + 2

    #OP99: Exit. Returns -1, indicating program completed siccessfully.
    elif code[p] == 99:
      return -1

    #Any other opcode. Returns -2, indicating a failure somewhere.
    else:
      print("ERROR: Unexpected OPCODE: " + str(code[p]))
      return -2

  def out(self):
    return self.output.pop()

class Droid:
  def __init__(self, filename):
    self.x = 0
    self.y = 0
    self.prog = Intcode(filename)

  def runMaze(self):
    moves = deque([1,2,3,4])
    steps = 0
    while True:
      nextMove = moves.popleft()
      if nextMove > 0:  
        self.prog.run(nextMove, 1)
        output = self.prog.out()
        if output == 1:
          steps += 1
          self.makeMoves(moves, nextMove)
        if output == 2:
          print("Gotcha!")
          return steps
      else:
        steps += -1
        self.prog.run(-1 * nextMove, 1)

  #Add the three moves (nextMove and both tangentials) and negative opposite nextMove
  def makeMoves(self, moves, lastMove):
    if lastMove < 0:
      lastMove *= -1
    if lastMove == 1:
      enque = [-2, 1, 4, 3]
    elif lastMove == 2:
      enque = [-1, 4, 3, 2]
    elif lastMove == 3:
      enque = [-4, 3, 2, 1]
    else:
      enque = [-3, 4, 2, 1]
    moves.extendleft(enque)


droid = Droid("droid")
step = droid.runMaze()
print(step)