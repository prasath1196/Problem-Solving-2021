class Solution:

    def findMaxGuests(self, Entry, Exit, N):
        max_size = max(max(Entry), max(Exit))
        store = {}
        for i in range(max_size+1):
          store[i] = {"in": 0, "out": 0} 
        for i in range(N):
            store[Entry[i]]["in"] += 1 
            store[Exit[i]]["out"] += 1  
        max_guests = [0,0]
        max_so_far = 0
        number_of_guests_in =  0
        for i in store:
          number_of_guests_in =  number_of_guests_in + store[i]["in"]
          if ( number_of_guests_in > max_so_far ):
            max_so_far =  number_of_guests_in
            max_guests = [i, number_of_guests_in]
          number_of_guests_in = number_of_guests_in - store[i]["out"]
        return max_guests
          

if __name__ == '__main__':
  t =  int(input())
  for _ in range(1):
    N = int(input())

    Entry = [int(x) for x in input().split()]
    Exit =  [int(x) for x in input().split()]
    solObj = Solution()
    ans = solObj.findMaxGuests(Entry,Exit,N)
    print(ans[0],ans[1])