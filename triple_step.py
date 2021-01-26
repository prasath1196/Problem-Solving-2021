### QUESTION######
# A child is running up a staircase with n steps and can hop either 1 step, 2 step, or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up the stairs


    
def number_of_ways(n,store):
    if (n < 0):
      return 0
    elif( n == 0):
        return 1
    elif store[n] > -1:
        return store[n]
    else:
        store[n] = number_of_ways(n-1,store) + number_of_ways(n-2,store) + number_of_ways(n-3,store)
        return store[n]

store = [-1]*6
print(number_of_ways(5,store))