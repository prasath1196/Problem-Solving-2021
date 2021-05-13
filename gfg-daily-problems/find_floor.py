def binSearch(A,start,end,nearest_so_far,ele):
  midpoint = (start+end)//2
  if start >  end:
      return nearest_so_far
  elif A[midpoint] == ele:
      nearest_so_far = midpoint
      return nearest_so_far
  elif A[midpoint] > ele:
      return binSearch(A,start,midpoint-1,nearest_so_far,ele)
  elif A[midpoint] < ele:
      nearest_so_far = midpoint
      return binSearch(A,midpoint+1,end,nearest_so_far,ele)
              
      
  
  #Complete this function
def findFloor(A,N,X):
  return binSearch(A,0,N-1,-1,X)
  #Your code here

if __name__ == "__main__":
  print(findFloor([1,2,8,10,11,12,19],7,0))