"""
Leetcode Problem 20: Valid Parentheses (Easy)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:

    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

Complexity for this solution:
Time complexity of this solution is O(n), with n being the length of the string.
Space complexity is O(n) in the worst case, O(1) otherwise.

Source: https://www.youtube.com/watch?v=hlbuyOgxHbs
"""

def is_valid(string):
    
    # Save the opening parentheses here and pop them
    # when a closing parenthesis comes up
    parentheses = []
    
    for i in range(len(string)):
        if is_open(string[i]):
            parentheses.append(string[i])
        else:
            # In this case, there is definitely a closing parenthesis too much
            # --> not valid
            if len(parentheses) == 0:
                return False
            # Now compare the last opening parenthesis
            # with the closing one just found
            if not is_same_type(parentheses.pop(), string[i]):
                return False
    
    # Final check: If the length is not 0,
    # there was an opening parenthesis too much
    return len(parentheses) == 0

# helper 1
def is_open(parenthesis):
    if parenthesis == '(' or parenthesis == '[' or parenthesis == '{':
        return True
    else:
        return False

# helper 2
def is_same_type(opening, closing):
    if opening == '(' and closing == ')': return True
    elif opening == '{' and closing == '}': return True
    elif opening == '[' and closing == ']': return True
    else: return False

# Testing --------------------------------------------------------------------  
def main():
    string = "({(())}[])"
    print(is_valid(string))

if __name__ == '__main__':
    main()