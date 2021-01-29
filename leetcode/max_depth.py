"""
Leetcode Problem 104:

Given a binary tree, what is the maximumm depth of the tree?

Time and space complexity is O(n) with n being the nuber of nodes in the tree.
Average space complexity is O(log n) for a balanced tree.
"""

# Node implementation ------------------------------------------------------------------
class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, value):  
        self.value = value
        self.left = None
        self.right = None

# This is my initial solution: --------------------------------------------------
def max_depth(root):
    
    if root.value is None: return 0
    
    depth = 1
    
    depth_left = max_depth(root.left) if root.left is not None else 0
    depth_right = max_depth(root.right) if root.right is not None else 0
    
    depth += max(depth_left, depth_right)
    
    return depth

# Optimized code: ------------------------------------------------------------------
def max_depth_alternative(root):
    
    if root.value is None: return 0

    depth_left = max_depth(root.left) if root.left is not None else 0
    depth_right = max_depth(root.right) if root.right is not None else 0
    depth = 1 + max(depth_left, depth_right)
    
    return depth

# Testing ---------------------------------------------------------------------------- 
if __name__ == '__main__':
      
    # Test 1:
    root = newNode(5)
    
    root.left = newNode(4)
    root.right = newNode(7)
    root.right.left = newNode(6)
    root.right.right = newNode(9)
    root.right.left.left = newNode(3)
    root.right.left.left.right = newNode(10)
    
    print("The depth of the tree is:", max_depth(root))
    
    
    # Test 2: Empty tree
    root = newNode(None)
    
    print("The depth of the tree is:", max_depth(root))
    
    
    # Test 3: Single node tree
    root = newNode(1)
    
    print("The depth of the tree is:", max_depth(root))