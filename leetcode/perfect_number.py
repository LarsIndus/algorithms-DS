"""
Leetcode Problem 507: Perfect Number (Easy)

A perfect number is a positive integer that is equal to the sum of its positive divisors,
excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

O(sqrt(n)) time and O(1) space
"""

import math

def is_perfect(n):
    
    if n > 1:
        i = 2
        sum_of_divisors = 1
        while i <= math.sqrt(n):
            if n % i == 0:
                sum_of_divisors += i
                sum_of_divisors += n / i
            i += 1
            
        return sum_of_divisors == n
    
    return False

# This function also outputs the divisors
def is_perfect_print(n):
    
    if n > 1:
        i = 2
        divisors = [1]
        while i <= math.sqrt(n):
            if n % i == 0:
                divisors.append(i)
                divisors.append(n // i)
            i += 1
            
        if sum(divisors) == n:
            divisors.sort()
            return divisors
    
    print(n, "is not a perfect number.")

# Testing --------------------------------------------------------------------
def main():
    n = 28
    print(str(n) + ": " + str(is_perfect(n)) + " (expected: True)")

    n = 14
    print(str(n) + ": " + str(is_perfect(n)) + " (expected: False)")

if __name__ == '__main__':
    main()