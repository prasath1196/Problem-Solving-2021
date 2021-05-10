import heapq 

def minCost(arr,n) :
    heapq.heapify(arr)
    res = 0   
    while(len(arr) > 1 ):
      v1 =  heapq.heappop(arr)
      v2 =  heapq.heappop(arr)
      res += v1 + v2
      heapq.heappush(arr,v1+v2)
    return res

if __name__ == "__main__":
  print(minCost([4,2,7,6,9],4))