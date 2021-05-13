import Math
arr = [7, 8, 19, 7, 8, 7, 10, 20]
req_sum = 38
n = 8
arr.sort(reverse=True)
head =  0
itr = 1
best_so_far = []
towers_built = 0

while(head <= n-1):
  curr_sum = arr[head]
  if (arr[head] >= req_sum):
    best_diff = Math.abs(head - req_sum)
    best_so_far.append(head)
  else:
    while(itr <= n-1)  
