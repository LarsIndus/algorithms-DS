# This script takes a string and returns the longest palindromic substring.
# Time complexity: O(n^2)
# Space complexity: O(1) (use three pointers, see below)

# First, define a helper function that returns the largest palindromic substring
# starting from a left and right index (by gradually moving them outwards if matching characters are found).
def largest_palindrome_at_index(s, left, right):
    
    left_index = 0
    right_index = 0
    
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            left_index = left
            right_index = right
        else:
            break
        left -= 1
        right += 1
        
    return s[left_index : right_index + 1]

# Main function: traverse through the list using the helper function from above
def longest_palindrome(s):
    
    result = ""  
    for i in range(len(s)):
        palindrome_odd = largest_palindrome_at_index(s, i, i)
        palindrome_even = largest_palindrome_at_index(s, i, i + 1)
        larger_palindrome = palindrome_odd if len(palindrome_odd) > len(palindrome_even) else palindrome_even
        result = result if len(result) >= len(larger_palindrome) else larger_palindrome
        
    return result