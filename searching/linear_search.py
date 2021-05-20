# Linear search has time complexity O(n) and also works on unsorted lists.

def linear_search(my_list, key):
    i = 0
    while i < len(my_list) and my_list[i] != key:
        i += 1
        
    if i < len(my_list):
        result = i
    else:
        result = -1
        
    return result

# Testing --------------------------------------------------------------------
def main():
    my_list = [4, 3, 2, 1, 5, 7, 6]

    r = linear_search(my_list, 3)
    if r == 1:
        print("Test A passed")
    else:
        print("Test A failed. Expected 1 and got", r)
    
    r = linear_search(my_list, 2)
    if r == 2:
        print("Test B passed")
    else:
        print("Test B failed. Expected 2 and got", r)
    
    r = linear_search(my_list, 10)
    if r == -1:
        print("Test C passed")
    else:
        print("Test C failed. Expected -1 and got", r)

if __name__ == '__main__':
    main()