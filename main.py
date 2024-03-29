from collections import deque
from Intcode.intcode import Intcode

#we have a workable base but this implementation assumes no box loops.
#instead let's map as we go. Bonus points for using return to stop manually and visually represent the map.




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


droid = Droid("input")
step = droid.runMaze()
print(step)