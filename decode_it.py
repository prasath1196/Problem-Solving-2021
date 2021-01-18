# cook your dish here
import string 

letters = list(string.ascii_lowercase)[0:16]
for _ in range(int(input())):
    n = int(input())
    encoded = input()
    # print(encoded)
    i = 0
    res = []
    # print(encoded)
    while(i < n):
        res.append(letters[int(''.join(encoded[i:i+4]),2)])
        i = i+4
    print(''.join(res))
    