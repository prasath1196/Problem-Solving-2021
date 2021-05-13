import sys
t =  int(raw_input())
while(t):
  n,k = map(int,raw_input().split())
  arr = list(map(int,raw_input().split()))
  minimum_moves = sys.maxsize
  min_index = -1
  for i in range(n):
    if arr[i] < k and k%arr[i] == 0 and (k/arr[i]) < minimum_moves:
       minimum_moves = (k/arr[i])
       min_index = i
  result = -1
  if min_index != -1: result = arr[min_index]
  print(result)
  t -= 1