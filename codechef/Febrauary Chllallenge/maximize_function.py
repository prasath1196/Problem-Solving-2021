def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split(' ')))
    arr.sort(reverse=True)
    z =  arr[0]
    x =  arr[n-1]
    y = arr[n/2]
    if n%2 == 0:
      sum1 = abs(x - (arr[n/2])) + abs(arr[n/2] - z)
      sum2 = abs(x -  arr[(n-1)/2]) + abs( arr[(n-1)/2] - z )
      if sum1 > sum2:
        y = arr[n/2]
      else:
        y = arr[(n-1)/2]
    print(abs(x-y) + abs(y-z) + abs(z-x))

if __name__ == "__main__":
  main()