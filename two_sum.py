# Given an array of integers, return two indices such that the respective values
# add up to a given target value.
# We can suppose that the problem can be solved uniquely.

def two_sum(arr, target):
    complements = {}
    result = []
    for index, num in enumerate(arr):
        if complements.get(num) is None:
            complements[target - num] = index
        else:
            result = [complements[num], index]
    return result