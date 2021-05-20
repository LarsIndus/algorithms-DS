"""
Leetcode Problem 17: Letter Combinations of a Phone Number (Medium)

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Complexity for this solution:
Time and space complexity is O(4^n) (as there are at most 4 characters on a number button).

Solution: https://www.youtube.com/watch?v=s1TuIgs1gMs
"""

def letter_combinations(digits):
    sol = []
    if len(digits) == 0: return sol
    letter_combinations_helper(digits, '', sol)
    return sol

def letter_combinations_helper(digits, curr, sol):
    if len(digits) == 0:
        sol.append(curr)
        return
    
    possible_chars = digit_to_letters(digits[0])
    for char in possible_chars:
        curr += char
        letter_combinations_helper(digits[1 : ], curr, sol)
        curr = curr[ : -1]

def digit_to_letters(digit):
    mapping = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
    }
    return mapping[digit]

# Testing --------------------------------------------------------------------
def main():
    digits = "283"
    print(letter_combinations(digits))

if __name__ == '__main__':
    main()