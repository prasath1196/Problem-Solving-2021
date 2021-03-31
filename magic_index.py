def find_magic_index(arr,n):
  return search_index(arr,0,n)

def search_index(arr,start,end):
  if end < start:
    return -1 
  mid =  (start + end)//2
  if (arr[mid] ==  mid ):
    return mid 
  else:
    left_index = min(mid-1, arr[mid])
    left = search_index(arr,start,left_index)
    if (left >= 0):
      return left 
    right_index = max(mid+1,arr[mid])
    right =  search_index(arr,right_index,end)
    if (right >= 0):
      return right
def main():
  n =  int(input())
  arr =  list(map(int,input().split(" ")))
  print(find_magic_index(arr,n))
if __name__ == "__main__":
  main()