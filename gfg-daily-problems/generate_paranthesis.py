def countSetBit(n):
  count = 0
  for i in range(4*8):
    if(n & (1 << i)):
      count += 1
  return count
def AllParenthesis(n):
  str = [""] *2*n
  res = []
  if(n > 0):
      _printParenthesis(str, 0,n, 0, 0,res)
  return res;
 
def _printParenthesis(str, pos, n,open, close,res):
  if(close == n):
      res.append("".join(str))
      return
  else:
      if(open > close):
          str[pos] = ')'
          _printParenthesis(str, pos + 1, n,open, close + 1,res);
      if(open < n):
          str[pos] = '('
          _printParenthesis(str, pos + 1, n,open + 1, close,res);

if __name__ == "__main__":
  print(AllParenthesis(3))