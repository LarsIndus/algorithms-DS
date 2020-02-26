# Leetcode Problem 98:

# Source: https://www.youtube.com/watch?v=ofuXorE-JKE

# Node implementation ------------------------------------------------------------------
class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, data):  
        self.data = data 
        self.left = None
        self.right = None

# Solution -----------------------------------------------------------------------------
def is_valid_BST(root):
    return helper(root, float("-inf"), float("inf"))

def helper(root, min_value, max_value):
    if root is None:
        return True
    if root.data < min_value or root.data > max_value:
        return False
    
    valid_left = helper(root.left, min_value, root.data)
    valid_right = helper(root.right, root.data, max_value)
    
    return valid_left and valid_right
        
        
# Testing -------------------------------------------------------------------------------

if __name__ == '__main__':
    
    # Test 1: Empty tree
    tree = None
    if is_valid_BST(tree):
        print("Passed test 1 (emtpy tree).")
    else:
        print("Test 1 (empty tree) failed!")
    
    # Test 2: Only root node
    tree = newNode(1)
    if is_valid_BST(tree):
        print("Passed test 2 (only root node).")
    else:
        print("Test 2 (only root node) failed!")
    
    # Test 3: Valid BST
    tree = newNode(2)
    tree.left = newNode(1)
    tree.right = newNode(3)
    tree.left.left = newNode(0)
    tree.right.left = newNode(2)
    tree.right.right = newNode(9)
    
    if is_valid_BST(tree):
        print("Passed test 3 (valid tree).")
    else:
        print("Test 3 (valid tree) failed!")
    
    # Test 4: Non-valid BST
    tree = newNode(2)
    tree.left = newNode(1)
    tree.right = newNode(3)
    tree.left.left = newNode(0)
    tree.right.left = newNode(1)
    tree.right.right = newNode(9)
    
    if not is_valid_BST(tree):
        print("Passed test 4 (non-valid tree).")
    else:
        print("Test 4 (non-valid tree) failed!")
    