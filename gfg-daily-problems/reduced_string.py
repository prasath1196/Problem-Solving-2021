from collections import deque

def Reduced_String(self, k, s):
  if k == 1:
      ret = ''
      return ret
  
  q = deque()
  
  for c in s:
      # entries in deque will consist of a char
      # and an integer representing how many times it is repeating
      if len(q) and q[-1][0]==c:
          q[-1][1] += 1           # incrementing count
          if q[-1][1]==k:
              q.pop()             # popping if count is k
      else:
          q.append( [c,1] )       # adding new character
  
  ret=''
  while len(q):                   # generating output string
      ret += q[0][0] * q[0][1]
      q.popleft()
  
  return ret 

if __name__ == "__main__":
  print(Reduced_String(2,"geeksforgeeks"))
