from collections import deque
def removeKdigits(S, k):
    n = len(S)
    res = []
    stack = deque()
    for i in range(len(S)):
        if n == k:
            res = "0"
            break
        else:
            if stack:
                while(stack and k > 0 and stack[-1] > int(S[i])):
                    stack.pop()
                    k = k-1
                stack.append(int(S[i]))
            else:
                stack.append(int(S[i]))
    while(k>0):
        stack.pop()
        k= k-1
    while(stack):
        res.append(stack.pop())

    res = list(map(str,res))
    res.reverse()
    return int("".join(res))

if __name__ == "__main__":
  print(removeKdigits("1002991",3))