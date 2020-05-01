def getNextPhase(oldSig):
  BASE = (0, 1, 0, -1)
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

def runFFT(fn, numPhases):
  with open(fn, "r") as f: signal = f.read().strip()
  nextSig = signal
  for i in range(numPhases): nextSig = getNextPhase(nextSig)
  print ("Finished. Result is " + nextSig[:8])


def bigFFT(fn, numPhases):
  with open(fn, "r") as f: signal = f.read().strip()
  nextSig = ([int(x) for x in signal] * 10000)[int(signal[:7]):]
  for _ in range(numPhases): 
    for i in range(len(nextSig) - 1, 0, -1):
      nextSig[i-1] = (nextSig[i-1] + nextSig[i]) % 10
  print ("Finished. Result is " + ''.join(str(x) for x in nextSig[:8]))


def main():
  #runFFT('biginput', 100)
  bigFFT('biginput', 100)
  
if __name__ == "__main__":
  main()