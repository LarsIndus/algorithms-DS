"""
Leetcode Problem 242: Valid Anagram (Easy)

Given two strings s and t , write a function to determine if t is an anagram of s.

Complexity for this solution:
O(max(n, m)) time (where n, m are the lenghts of the strings)
and O(1) space (only 26 characters!).
"""

def is_anagram(s1, s2):
    
    # Strip white spaces and convert to lower case.
    # This way, we can also check whole phrases rather than just single words.
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2): return False
    
    letters1 = {}
    letters2 = {}
      
    for char in s1:
        if char in letters1:
            letters1[char] += 1
        else:
            letters1[char] = 1
    
    for char in s2:
        if char in letters2:
            letters2[char] += 1
        else:
            letters2[char] = 1
    
    print(letters1)
    print(letters2)
    return letters1 == letters2

# In an alternative solution, we can use just one dictionary.
# The first for loop will be the same,
# the second uses the same dictionary but decrements the values.
# In the end, we check whether all values are 0.

def is_anagram_alternative(s1, s2):
    
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2): return False
    
    letters = {}
      
    for char in s1:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    
    for char in s2:
        if char in letters:
            letters[char] -= 1
        else: return False
    
    print(letters)
    for letter in letters.keys():
        if letters[letter] != 0: return False
        
    return True

# Testing --------------------------------------------------------------------    
def main():
    s1 = "anagram"
    s2 ="nagaram"
    print(is_anagram(s1, s2))

if __name__ == '__main__':
    main()