# Small is 1kg, Big is 5kg 
# We need to find how to get to the goal(in kg)
# with a given number of small and big bars
# Solved: November 3rd, 2020

def make_chocolate(small, big, goal):
  if big*5 <= goal:
      diff = goal - (big*5) 
  else: 
      diff = goal % 5

  if diff <= small:
      return diff
  else: 
      return -1
 

print(str(make_chocolate(6,1,10)))