n =  int(input())

greatest_so_far = 0

if n % 2 == 0:
  greatest_so_far = 2
else:
  greatest_so_far = 1

if n <=10: 
  print n
else:
  for i in range(10,1,-1):
    if n%i == 0:
      greatest_so_far = i  
      break
  print greatest_so_far