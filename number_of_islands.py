# Leetcode Problem 200:
# Given a two-dimensional grid of 1s (land) and 0s (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically.
# We may assume that all four edges of the grid are surrounded by water.
# Time complexity of this solution is O(nm), with n and m denoting the dimensions of the grid.
# Space complexity here is O(1).
# We can also use a 'visited' array of the same size as the grid, giving O(nm) space complexity,
# see the alternative solution.
#
# Source: https://www.youtube.com/watch?v=z5c2pJeMqOw


# Helper function: Depht-first search
def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return
    # Mark the visited entry with any placeholder that is not a 1:
    grid[i][j] = "#"
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)
    
def number_of_islands(grid):
    count = 0
    
    # Traverse through the grid and increase the counter every time a dfs is performed.
    # We do the dfs every time we find land.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                count += 1
                
    return count


# Alternative Solution -------------------------------------------------------------------------------

# In this solution we keep track of the visited fields in a separate array.
 
 # Helper function: Depth-first search
def dfs_alternative(grid, visited, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1 or visited[i][j]:
        return
    visited[i][j] = True
    dfs_alternative(grid, visited, i + 1, j)
    dfs_alternative(grid, visited, i - 1, j)
    dfs_alternative(grid, visited, i, j + 1)
    dfs_alternative(grid, visited, i, j - 1)

def number_of_islands_alternative(grid):
    
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    count = 0
    
    # Traverse through the grid and increase the counter every time a dfs is performed.
    # We do the dfs every time we find land.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == 1:
                dfs_alternative(grid, visited, i, j)
                count += 1
                
    return count