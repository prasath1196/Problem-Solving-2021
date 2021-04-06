def is_strong_language(word,k,n):
  res = "NO"
  count = 0
  for letter in word:
    if letter == "*":
      count+=1
    else: 
      if count == k: 
        res = "YES"
        break
      else:
        count = 0
  return res 


def main():
  t = int(input())
  while(t):
    n,k = map(int,input().split(" "))
    word = input()
    print(is_strong_language(word,k,n))
    t = t-1

if __name__ == "__main__":
  main()
  