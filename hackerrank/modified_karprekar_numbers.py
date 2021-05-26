#!/bin/python3

import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    res = []
    for i in range(p,q+1):
        d =  len(str(i))
        square =  str(i**2)
        
        no_of_digits = len((square))
        if no_of_digits == d: 
            if int(square) == i:
                res.append(i)
        else:
            r =  (square)[-d:]
            l =  (square)[:(no_of_digits-d)]
            if (int(r) + int(l)) == i:
                res.append(i)
    if len(res) == 0:
        print ("INVALID RANGE")
    else:
        print (" ".join(map(str,res)))
            
        
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
