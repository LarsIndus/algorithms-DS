# Given a staircase of n steps, how many possible ways to go up are there?
# The number of steps you can take at one time is given by the set 'steps'.

# In the beginning, let set = {1, 2}.
# Start with basic cases:
# Obviously, num_ways(0) = 1, num_ways(1) = 1 and num_ways(2) = 2.
def num_ways_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways_recursive(n - 1) + num_ways_recursive(n - 2)
    
# Note that this function is just the fibonacci series.
# However, due to the recursion, it's not efficient.
# Check this bottom up approach instead (dynamic programing):

def num_ways_bottom_up(n):
    if n == 0 or n == 1 :
        return 1
    
    # initialize an array to store the values and define base cases.
    nums =  [0] * (n + 1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n + 1):
        nums[i] = nums[i - 1] + nums[i - 2]
    return nums[n]


# Next, consider the variation with a given number of steps possible at one time.
# Again, we start with a recursive approach.
def num_ways_steps(n, steps):
    if n == 0:
        return 1
    
    total = 0
    for i in steps:
        if n - i >= 0:
            total += num_ways_steps(n - i, steps)
    return total

# As before, here's a bottom up version of the above function:
def num_ways_steps_bottom_up(n, steps):
    if n == 0:
        return 1
    nums = [0] * (n + 1)
    nums[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in steps:
            if i - j >= 0:
                total += nums[i - j]
        nums[i] = total
    return nums[n]

# Testing --------------------------------------------------------------------
def main():
    n = 5
    steps = {1, 2, 3}
    print("n = ", n, ", steps = ", steps, ". Possible ways: ",
          num_ways_steps_bottom_up(n, steps), sep = "")

if __name__ == '__main__':
    main()