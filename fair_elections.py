for _ in range(int(input())):
	n,m = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	swap_count = 0
	difference = sum(b) - sum(a)
	if difference < 0:
		print("0")
	elif min(a) >= max(b):
		print("-1")
	else:
		while(sum(a) < sum(b) and swap_count < len(b)):
			total = min(a) + max(b)
			a[a.index(min(a))] = total - min(a)
			b[b.index(max(b))] = total - max(b)
			swap_count+=1
		print(swap_count)
