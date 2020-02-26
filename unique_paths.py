# Leetcode Problem 62:
# Given an nxm matrix, how many paths are there going from the
# top left corner to the bottom right corner
# if we can only move to the right and down?
# Time and space complexity of this solution is O(nm).
#
# Source: https://www.youtube.com/watch?v=RYpd5VzxlKQ

def unique_paths(n, m):
    
    mat = [[1 for j in range(m)] for i in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
            
    return mat[n - 1][m - 1]