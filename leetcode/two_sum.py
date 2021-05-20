"""
Leetcode Problem 1: Two Sum (Easy)

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Complexity for this solution:
...

Solution: https://www.youtube.com/watch?v=s1TuIgs1gMs
"""

def two_sum(arr, target):
    complements = {}
    result = []
    for index, num in enumerate(arr):
        if complements.get(num) is None:
            complements[target - num] = index
        else:
            result = [complements[num], index]
    return result

# Testing --------------------------------------------------------------------      
def main():
    arr = [2, 5, 6, 11]
    target = 16
    print(two_sum(arr, target))

if __name__ == '__main__':
    main()