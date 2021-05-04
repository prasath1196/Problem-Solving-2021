class Solution:
    
    def no_of_1s(self,row,start,end):
        midpoint = (start + (end - start))//2
        res = 0 
        if midpoint == 0:
            if row[midpoint] == 1:
                return 1
            else: 
                return 0
        if row[midpoint] == 1: 
            for i in range(0,midpoint):
                if row[i] == 1:
                    res = end - i
                    break
        else: 
            for i in range(midpoint+1,end):
                if row[i] == 1:
                    res = end - i
                    break
        return res 
	def rowWithMax1s(self,arr, n, m):
	    max_so_far = -1 
        index = -1 
        for i in range(n):
            row = arr[i] 
            res = self.no_of_1s(row,0,m)
            if res > max_so_far:
                max_so_far = res 
                index = i 
        if max_so_far == 0:
            index = -1
        return index 


if __name__ == "__main__":
  arr= [[0,0,0,0],[1,1,1,1],[0,0,0,1],[0,1,1,1]]
  n = 4 
  m = 4 
  print(rowWithMax1s(arr,n,m))


  