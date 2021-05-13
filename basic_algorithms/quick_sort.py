class Solution:
    
    
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            p =  self.partition(arr,low,high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
    
    def partition(self,arr,low,high):
        i =  low - 1
        pivot = arr[high]
        for j in range(low,high):
            
            if (arr[j] < pivot): 
                i +=1
                temp = arr[i]
                arr[i]=arr[j]
                arr[j] =  temp
        temp = arr[high]
        arr[high]=arr[i+1]
        arr[i+1] =  temp
        return i+1