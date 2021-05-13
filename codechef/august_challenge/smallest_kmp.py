from itertools import permutations 
  
def lexicographical_permutation(str): 
    perm = sorted(''.join(chars) for chars in permutations(str)) 
    for x in perm: 
        print(x) 
          
str ='abc'
import string
t = int(raw_input())
while(t):
    result =""
    s = raw_input()
    p = raw_input()
    alpha_counter = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in s:
      alpha_counter[letter] += 1
    for letter in p:
      alpha_counter[letter] -= 1
    start_letter = p[0]
    start_index = 0
    for k,v in sorted(alpha_counter.items()):
      if k <= p[start_index]:
        if start_index == 0:
            p = v*k + p
        else:
            p = p[0:(start_index)] + v*k + p[start_index:]
        start_index += v
      else:
        p = p + v*k 
    print(p)
    print(lexicographical_permutation(s))
    t -= 1


