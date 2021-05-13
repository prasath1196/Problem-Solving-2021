
from datetime import date, time, datetime

def convert_to_24hrs(t,meridiam): 
  hour =  t[0:2]
  minutes = t[3:]
  if meridiam == "AM" and hour == "12":
    hour_24 = 00 
  elif meridiam == "PM" and hour != "12":
    hour_24 = int(hour) + 12
  else:
    hour_24 =  int(hour) 
  minutes_24 = int(minutes)
  return time(hour_24,minutes_24)
def main():
  t = int(input())
  for _ in range(t):
    res = []
    p,p_meridiam = input().split(' ')
    p_24 = convert_to_24hrs(p,p_meridiam) 
    n =  int(input())
    for _ in range(n):
      left, left_meridiam,right,right_meridiam = input().split(' ')
      r = convert_to_24hrs(right,right_meridiam)
      l = convert_to_24hrs(left,left_meridiam)
      print(p_24,l,r)
      if p_24 >= l and p_24 <=r: 
        res.append('1')
      else:
        res.append('0')
    print(''.join(res))

      

if __name__ == "__main__":
    main()