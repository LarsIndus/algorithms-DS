# Binary search has time complexity O(log n) but only works on sorted lists.

# The first implementation uses iteration.
def binary_search(my_list, key):
    lower_bound = 0
    upper_bound = len(my_list) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        
        middle_pos = (upper_bound + lower_bound) // 2
    
        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    
    if found == True:
        result = middle_pos
    else:
        result = -1
        
    return result


# The second implementation uses recursion.
def binary_search_recursive(my_list, key, lower_bound, upper_bound):
    
    if upper_bound < lower_bound:
        return -1
    
    middle_pos = (upper_bound + lower_bound) // 2
    if my_list[middle_pos] == key:
        return middle_pos
    elif my_list[middle_pos] < key:
        return binary_search_recursive(my_list, key, middle_pos + 1, upper_bound)
    else:
        return binary_search_recursive(my_list, key, lower_bound, middle_pos - 1)


# Test the two functions:
my_list = [0, 3, 5, 12, 18, 50, 70, 78]

# 1. iterative method
r = binary_search(my_list, 3)
if r == 1:
    print("Test A passed (iterative).")
else:
    print("Test A failed (iterative). Expected 1 and got", r)
 
r = binary_search(my_list, 5)
if r == 2:
    print("Test B passed (iterative).")
else:
    print("Test B failed (iterative). Expected 2 and got", r)
 
r = binary_search(my_list, 10)
if r == -1:
    print("Test C passed (iterative).")
else:
    print("Test C failed (iterative). Expected -1 and got", r)


# 2. recursive method
r = binary_search_recursive(my_list, 3, 0, len(my_list) - 1)
if r == 1:
    print("Test A passed (recursive).")
else:
    print("Test A failed (recursive). Expected 1 and got", r)
 
r = binary_search_recursive(my_list, 5, 0, len(my_list) - 1)
if r == 2:
    print("Test B passed (recursive).")
else:
    print("Test B failed (recursive). Expected 2 and got", r)
 
r = binary_search_recursive(my_list, 10, 0, len(my_list) - 1)
if r == -1:
    print("Test C passed (recursive).")
else:
    print("Test C failed (recursive). Expected -1 and got", r)