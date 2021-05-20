"""
Leetcode Problem 62: Unique Paths (Medium)

A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

Complexity for this solution:
O(nm) time and space (linear in grid size)

Source: https://www.youtube.com/watch?v=RYpd5VzxlKQ
"""

def unique_paths(n, m):
    
    mat = [[1 for j in range(m)] for i in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
            
    return mat[n - 1][m - 1]

# Testing --------------------------------------------------------------------
def main():
    n = 3
    m = 5
    print(unique_paths(n, m))

if __name__ == '__main__':
    main()