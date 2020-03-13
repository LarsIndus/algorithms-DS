# Mergesort is O(n * log(n)) (worst, best and average).
# It is not in-place but stable.

import random

def mergeSort(arr):
    
    if len(arr) > 1: 
        mid = len(arr) // 2 # Finding the mid of the array 
        left = arr[ : mid] # Dividing the array elements  
        right = arr[mid : ] # into 2 halves 
  
        mergeSort(left) # Sorting the first half 
        mergeSort(right) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays left[] and right[] 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j += 1
            k += 1
          
        # Checking if any element was left 
        while i < len(left): 
            arr[k] = left[i] 
            i += 1
            k += 1
          
        while j < len(right): 
            arr[k] = right[j] 
            j += 1
            k += 1
  
# Testing the code:  
if __name__ == '__main__':  
    def print_list(my_list):
        for item in my_list:
            print("{:3}".format(item), end="")
        print()

    my_list = []
    for i in range(10):
        my_list.append(random.randrange(100))
    
    # Try out the sort
    print_list(my_list)
    mergeSort(my_list)
    print_list(my_list)