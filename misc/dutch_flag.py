# Dutch flag problem (sort an array of 0s, 1s and 2s).
def dutch_flag_sorting(arr):
    
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while mid <= high: 
        if arr[mid] == 0: 
            arr[low], arr[mid] = arr[mid], arr[low] 
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1: 
            mid = mid + 1
        else: 
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
            
    return arr

def print_array(arr): 
    for k in arr: 
        print(k)
    print()


if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
    arr = dutch_flag_sorting(arr)
    print_array(arr)
         