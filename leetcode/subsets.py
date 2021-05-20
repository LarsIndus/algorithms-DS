"""
Leetcode Problem 78: Subsets (Medium)

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Complexity for this solution:
O(n * 2^n) time and space (2^n subsets and traverse at most n times to generate each subset).
If we don't consider the space for the final result, space complexity becomes O(n)
(e.g., when just asked to print the subsets instead of saving them).

Source: https://www.youtube.com/watch?v=LiuEfq37hqc
"""

def subsets(nums):
    sol = []
    helper(nums, sol, [], 0)
    return sol

def helper(nums, sol, curr, index):
    #print(curr, index)
    sol.append(list(curr))
    for i in range(index, len(nums)):
        curr.append(nums[i])
        helper(nums, sol, curr, i + 1)
        # 'pop' returns a value, but we don't need that.
        # We can just delete the last value using 'del'.
        #curr.pop()
        del curr[-1]

# Testing --------------------------------------------------------------------
def main():
    nums = [1, 2, 3]
    power_set = subsets(nums)
    print(power_set)

if __name__ == '__main__':
    main()