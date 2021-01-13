# cook your dish here

def find_top_right(start,n):
    x,y = start
    if x > y: 
      return [n, n-(x-y)]
    else:
      return [n-(y-x),n]
def find_top_left(start,n):
    x,y = start
    return [y,x]
def find_bottom_right(start,n):
    x,y = start
    return [y,x]
def find_bottom_left(start,n):
    x,y = start
    if x > y:
      return [x-y,0]
    else:
      return [0,y-x]
    
for _ in range(int(input())):
    n,k,x,y = map(int,input().split())
    start = [x,y]
    if x==y:
        print(" ".join(map(str,[n,n])))
    else:
        contact_points = []
        
        if (x>y):
            first  = find_top_right(start,n)
            second = find_top_left(first,n)
            third  = find_bottom_left(second,n)
            fourth = find_bottom_right(third,n)
        else:
            first  = find_top_right(start,n)
            second = find_bottom_right(first,n)
            third  = find_bottom_left(second,n)
            fourth = find_top_left(third,n)
        contact_points = [first,second,third,fourth]
        if (k%4) == 0:
          index  = 3
        else:
          index = (k%4)-1
        print(contact_points)
        print(" ".join(map(str,contact_points[index])))