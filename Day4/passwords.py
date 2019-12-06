#passwords.py
#by Giovanni Prinzivalli
#06 December, 2019

class testIO:
  def mini(): return 387638
  def maxi(): return 919123

def isAscending(password):
  m = 10

  while password > 0:
    nextDigit = password % 10
    if nextDigit > m:
      return False
    else:
      password = int(password / 10)
      m = nextDigit

  return True

def isDoubled(password):
  for i in range(10):
    if str(password).count(str(i)) == 2:
      return True

  return False

def isValid(password):
  return isAscending(password) & isDoubled(password)

def countPasswords(mini, maxi):
  k = 0
  for i in range(mini, maxi):
    if isValid(i):
      k +=1
      
  return k

print(countPasswords(testIO.mini(), testIO.maxi()))