"""
Leetcode Problem 72: Edit Distance (Hard)

Given two words word1 and word2, find the minimum number of operations
required to convert word1 to word2.
You have the following 3 operations permitted on a word:

    1. Insert a character
    2. Delete a character
    3. Replace a character

Complexity for this solution:
...

Source: https://www.youtube.com/watch?v=hlbuyOgxHbs
"""

def edit_distance(word1, word2):
    
    mat = [[0 for j in range(len(word1) + 1)] for i in range(len(word2) + 1)]
    
    for i in range(len(word2) + 1):
        mat[i][0] = i
    
    for j in range(len(word1) + 1):
        mat[0][j] = j
        
    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            if word1[j - 1] == word2[i - 1]:
                mat[i][j] = mat[i - 1][j - 1]
            else:
                mat[i][j] = min(mat[i - 1][j], mat[i][j - 1],
                                mat[i - 1][j - 1]) + 1
            
    return mat[len(word2)][len(word1)]


# Another similar problem is to check whether the edit distance is exactly 1.
# Of course we could use the above function now,
# but there is also a direct approach.
# This solution has O(max(n,m)) time complexity and constant space complexity.

def edit_distance_one(word1, word2):
    
    n = len(word1)
    m = len(word2)
    
    if abs(n - m) > 1:
        print("Exited because difference in length too big.")
        return False
    
    edits = 0
    i = 0
    j = 0
    
    while i < n and j < m:
        
        # If the characters don't match, we need an edit.
        # If we already used an edit before, we
        # can exit the loop early (check below).
        if word1[i] != word2[j]:
            if edits > 0:
                print("Exited the loop, as number of edits exceeded 1 early.")
                return False
            edits += 1
        
        i += 1
        j += 1
    
    # If the length of the strings is not equal, thus 1
    # (because we excluded a difference > 1 above),
    # we need to continue one more time in the longer string
    # and we need an edit.
    if i < n:
        print("Checked i < n; i = ", i, " , j = ", j)
        edits += 1
    elif j < m:
        print("Checked j < m; i = ", i, " , j = ", j)
        edits += 1
    
    print("Exited at end of function; number of edits is ",
          edits, ".", sep = "")
    return edits == 1

# Testing --------------------------------------------------------------------
def main():
    word1 = "horse"
    word2 = "ros"
    print("Edit distance between '", word1, "' and '", word2, "': ",
          edit_distance(word1, word2), sep = "")

if __name__ == '__main__':
    main()


