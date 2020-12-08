# if any value is 13, then the sum will not move forward
# Solved: November 3rd, 2020

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a+b
  else:
    return a+b+c