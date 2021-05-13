# cook your dish here
t = int(input())
while(t):
    a,b = map(int,raw_input().split())
    if a <= 9:
        digits_a = 1
    else:
        digits_a = (a//9) 
        if a%9 !=0: digits_a +=1
    if b <= 9:
        digits_b = 1
    else:
        digits_b = (b//9)
        if b%9 !=0: digits_b +=1
    if digits_a == digits_b:
        winner = 1
        win_digits = digits_b
    elif digits_a > digits_b:
        winner  = 1
        win_digits = digits_b
    else:
        winner = 0
        win_digits = digits_a
    print (" ".join([str(winner),str(win_digits)]))
    t = t-1