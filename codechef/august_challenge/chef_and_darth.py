t = int(raw_input())
while(t):
  h,p = map(int,raw_input().split())
  if p > (h/2):
      print(1)
  else:
      print(0)
  t = t -1 