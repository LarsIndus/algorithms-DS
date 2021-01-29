"""
Leetcode Problem 78:

Given a set of distinct integers, return all possible subsets (i.e., the power set).
The solution must not contain duplicate subsets.

This solution has time and space complexity O(n * 2^n)
(2^n subsets and traverse at most n times to generate each subset).
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
        # 'pop' returns a value, but we don't need that. We can just delete the last value using 'del'.
        #curr.pop()
        del curr[-1]
        
if __name__ == '__main__':
    nums = [1, 2, 3]
    subsets = subsets(nums)
    print(subsets)