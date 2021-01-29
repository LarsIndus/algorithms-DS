"""
Leetcode Problem 112:

Given a binary tree and a target sum, decide whether there is a path
from the root node to a leave, such that the sum of all nodes in this path equals the sum.

Time and space complexity of this solution is O(n),
with n denoting the number of nodes in the tree.

Source: https://www.youtube.com/watch?v=IIPJ9tRYsg0
"""

# Node implementation ------------------------------------------------------------------
class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, data):  
        self.data = data 
        self.left = None
        self.right = None

# Solution -----------------------------------------------------------------------------
def path_sum(root, target):
    if root is None:
        return False
    elif root.left is None and root.right is None:
        return root.data == target
    
    target -= root.data
    return path_sum(root.left, target) or path_sum(root.right, target)


# Testing -----------------------------------------------------------------------

if __name__ == '__main__':
    
    # Test 1: Empty tree
    tree = None
    if not path_sum(tree, 1):
        print("Passed test 1 (emtpy tree).")
    else:
        print("Test 1 (empty tree) failed!")
    
    # Test 2: Only root node
    tree = newNode(1)
    if path_sum(tree, 1):
        print("Passed test 2 (only root node).")
    else:
        print("Test 2 (only root node) failed!")
    
    # Test 3: Only one leaf
    tree = newNode(1)
    tree.left = newNode(2)
    if path_sum(tree, 3):
        print("Passed test 3 (only one leaf).")
    else:
        print("Test 3 (only one leaf) failed!")
    
    # Test 4: Two leafs
    tree = newNode(1)
    tree.left = newNode(2)
    tree.right = newNode(3)
    if path_sum(tree, 3) and path_sum(tree, 4):
        print("Passed test 4 (two leaves).")
    else:
        print("Test 4 (two leaves) failed!")