def max_xor( arr , n):
     
    maxx = 0
    mask = 0;
 
    se = set()
     
    for i in range(30, -1, -1):
      mask |= (1 << i)
      newMaxx = maxx | (1 << i)
      for i in range(n):
        se.add(arr[i] & mask)
      for prefix in se:     
        if (newMaxx ^ prefix) in se:
            maxx = newMaxx
            break
      se.clear()
    return maxx


if __name__ == "__main__": 
  print(max_xor([25,10,2,8,5,3],6))