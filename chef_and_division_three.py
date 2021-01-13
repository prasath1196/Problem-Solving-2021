import math

for _ in range(int(input())):
	n,k,d = map(int,input().split())
	arr = list(map(int,input().split()))
	print(min( (sum(arr)//k), d))