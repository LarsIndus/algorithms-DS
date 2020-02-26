# Bubblesort is O(n^2) (average case and worst case), thus asymptotically not optimal.
# It is in-place and stable.

def bubblesort(arr):
    
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if (arr[j] > arr[j+1]): 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

# The above function always runs O(n^2) time even if the array is sorted.
# It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.

def bubblesort_optimized(arr):
    
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
   
            # Traverse the array from 0 to n-i-1.
            # Swap if the element found is greater than the next element 
            if (arr[j] > arr[j+1]): 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped by inner loop, then break 
        if swapped == False: 
            break
        
    return arr