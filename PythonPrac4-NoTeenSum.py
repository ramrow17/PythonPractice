def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):  
  if n > 12 and n < 20 and n != 15 and n != 16:
    return 0
  else:
    return n
   