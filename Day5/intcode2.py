#intcode2.py
#by Giovanni Prinzivalli
#06 December, 2019

def initArray(filename):
  code = []

  with open(filename, "r") as f:
    for instr in f.read().split(","):
      code.append(int(instr)) 

  return code

def operateOn(code):
  p = 0
  while p < len(code):
    opcode = code[p] % 100
    p1 = int(code[p] / 100) % 10
    p2 = int(code[p] / 1000) % 10
    p3 = int(code[p] / 10000)


    if opcode == 1:
      para1 = p+1 if p1 == 1 else code[p+1]
      para2 = p+2 if p2 == 1 else code[p+2]

      code[code[p+3]] = code[para1] + code[para2]
      p += 4

    elif opcode == 2:
      para1 = p+1 if p1 == 1 else code[p+1]
      para2 = p+2 if p2 == 1 else code[p+2]

      code[code[p+3]] = code[para1] * code[para2]
      p += 4

    #OP 3: Write. Input integer to location p1.
    elif opcode == 3:
      while True:
        try:
          code[code[p+1]] = int(input("Enter an integer: "))
        except ValueError:
          print("Ooops, that's  not an ID number!")
          continue
        else:
          break
      print("Success 3")
      p+=2
      
    #OP4: Read. Print value of location p1
    elif opcode == 4:
      para1 = p+1 if p1 == 1 else code[p+1]
      print("Value of location " + str(para1) + ": " + str(code[para1]))
      p+=2

    #OP5: Jump-if-true. If p+1 is nonzero, jump to p+2.
    elif opcode == 5:
      para1 = p+1 if p1 == 1 else code[p+1]
      para2 = p+2 if p2 == 1 else code[p+2]

      if code[para1] != 0:
        p = code[para2]
      else:
        p += 3

    #OP6: Jump-if-false: If p+1 is zerp, jump to p+2
    elif opcode == 6:
      para1 = p+1 if p1 == 1 else code[p+1]
      para2 = p+2 if p2 == 1 else code[p+2]

      if code[para1] == 0:
        p = code[para2]
      else:
        p += 3

    #OP7: Lesser. If p+1 is less than p+2, write 1 to p+3, else write 0.
    elif opcode == 7:
      para1 = p+1 if p1 == 1 else code[p+1]
      para2 = p+2 if p2 == 1 else code[p+2]

      code[code[p+3]] = 1 if code[para1] < code[para2] else 0
      p+=4
      
    #OP8: Equals. If p+1 equals p+2, write 1 to p+3, else write 0.  
    elif opcode == 8:
      para1 = p+1 if p1 == 1 else code[p+1]
      para2 = p+2 if p2 == 1 else code[p+2]

      code[code[p+3]] = 1 if code[para1] == code[para2] else 0
      p+=4

    elif code[p] == 99:
      return code

    else:
      print("Unexpected OPCODE: " + str(code[p]))
      return -1

  print("End of File.")
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

afterArray = operateOn(initArray("diagnostic"))