import time

def getNextPhase(oldSig):
  BASE = [0, 1, 0, -1]
  nextSig = ''  
  numDigs = len(oldSig)
  halfDigs = numDigs//2 - 1

  for i in range(numDigs):
    thisDigit = 0
    
    if i > halfDigs:
      for j in range(i, numDigs):
        thisDigit += int(oldSig[j])
    else:
      for j in range(numDigs):
        thisDigit += BASE[((j + 1) // (i + 1)) % 4] * int(oldSig[j])

    nextSig += str(abs(thisDigit) % 10)

  return nextSig

def runFFT(fn, numPhases, testFlag = False):
  #Pull the signal and expected result (if any) from the file.
  with open(fn, "r") as f:
    lines = [line.strip() for line in f.readlines()]
    signal = lines[0]
    if testFlag is True:
      expected = lines[1]

  #Pass the first signal into the function, then loop it x times.
  nextSig = signal
  for i in range(numPhases):
    nextSig = getNextPhase(nextSig)
  result = nextSig[:8]

  #Set up for writing to file and check the answer.
  if testFlag is True:
    lines = [signal + '\n', expected + '\n', result]
    if result == expected:
      print("Signal test file " + fn + " is correct.")
    else:
      print("Signal test file " + fn + " is incorrect.")
  else:
    lines = [signal + '\n', result]
    print ("Finished. Result is " + result)
  with open(fn, "w") as f:
    f.writelines(lines)

def main():
  runFFT('inputtest4', 1, True)
  runFFT('inputtest1', 100, True)
  runFFT('inputtest2', 100, True)
  runFFT('inputtest3', 100, True)

  runFFT('biginput', 100)
  
if __name__ == "__main__":