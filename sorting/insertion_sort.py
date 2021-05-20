# Insertion sort is stable and in-place.
# Its complexity is O(n^2) in the worst case and O(n) in the best case.

import random

def insertion_sort(my_list):
    """ Sort a list using the insertion sort """
 
    # Start at the second element (pos 1).
    # Use this element to insert into the list.
    for key_pos in range(1, len(my_list)):
 
        # Get the value of the element to insert
        key_value = my_list[key_pos]
 
        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1
 
        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
 
        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value
        

def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end = "")
    print()
 
# Testing --------------------------------------------------------------------
def main():
    my_list = []
    for i in range(10):
        my_list.append(random.randrange(100))
    
    # Try out the sort
    print_list(my_list)
    insertion_sort(my_list)
    print_list(my_list)

if __name__ == '__main__':
    main()