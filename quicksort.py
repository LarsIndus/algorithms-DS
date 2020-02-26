# Quicksort is O(n * log(n)) on average and O(n^2) in the worst case.
# It is in-place but not stable.

import random

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right of pivot
def partition(arr, low, high): 
    i = low              # index of smaller element 
    pivot = arr[high]    # pivot 

    for j in range(low, high): 

        # If current element is smaller than the pivot 
        if arr[j] < pivot: 
        
            # increment index of smaller element 
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i] 
    return i

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr, low, high): 
    if low < high: 

        # pi is partitioning index, arr[pi] is now 
        # at right place 
        pi = partition(arr, low, high) 

        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi - 1) 
        quickSort(arr, pi + 1, high) 


# Testing the code:    
def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end="")
    print()

my_list = []
for i in range(10):
    my_list.append(random.randrange(100))
 
# Try out the sort
print_list(my_list)
quickSort(my_list, 0, len(my_list) - 1)
print_list(my_list)
