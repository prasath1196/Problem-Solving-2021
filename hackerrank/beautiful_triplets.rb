#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr)
    n = arr.size 
    i = 0 
    j = 1 
    res = 0
    count = 0
    for i in 0..(n-d) do
        count = 0
        for j in (i+1)..(n-1) do 
            if (arr[j] - arr[i]) == d
                count =1
            elsif arr[j] - arr[i] == (2*d) and count == 1
                count =2
                res+= 1
                break 
            end
        end
    end
    res
end 

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

first_multiple_input = gets.rstrip.split

n = first_multiple_input[0].to_i

d = first_multiple_input[1].to_i

arr = gets.rstrip.split.map(&:to_i)

result = beautifulTriplets d, arr

fptr.write result
fptr.write "\n"

fptr.close()
