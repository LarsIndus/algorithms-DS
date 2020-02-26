# Leetcode Problem 78:
# Given a set of distinct integers, return all possible subsets (i.e., the power set).
# The solution must not contain duplicate subsets.
# This solution has time and space complexity O(2^n), due to the number of subsets.
#
# Source: https://www.youtube.com/watch?v=LiuEfq37hqc

def subsets(nums):
    sol = []
    helper(nums, sol, [], 0)
    return sol

def helper(nums, sol, curr, index):
    print(curr, index)
    sol.append(list(curr))
    for i in range(index, len(nums)):
        curr.append(nums[i])
        helper(nums, sol, curr, i + 1)
        # 'pop' returns a value, but we don't need that. We can just delete the last value using 'del'.
        #curr.pop()
        del curr[-1]