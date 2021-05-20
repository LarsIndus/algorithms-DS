"""
Leetcode Problem 100: Same Tree (Easy)

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.

Complexity for this solution:
O(n + m) with n, m being the number of nodes in the trees.

Source: https://www.geeksforgeeks.org/check-whether-the-two-binary-search-trees-are-identical-or-not/
(code slightly adjusted)
"""
  
# Node implementation --------------------------------------------------------
class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, data):  
        self.data = data 
        self.left = None
        self.right = None

# Solution -------------------------------------------------------------------
def is_identical(root1, root2):
  
    if root1 is None and root2 is None: return True
    if root1 is None or root2 is None: return False
    if root1.data != root2.data: return False
    
    is_identical_left = is_identical(root1.left, root2.left)
    is_identical_right = is_identical(root1.right, root2.right)

    return is_identical_left and is_identical_right
      
# Testing --------------------------------------------------------------------
def main():
      
    # Test 1: Non-empty identical trees:
    root1 = newNode(5)
    root2 = newNode(5)
    
    root1.left = newNode(3)
    root1.right = newNode(8)
    root1.left.left = newNode(2)
    root1.left.right = newNode(5)
  
    root2.left = newNode(3)
    root2.right = newNode(8)
    root2.left.left = newNode(2)
    root2.left.right = newNode(5)
  
    if (is_identical(root1, root2)):
        print("Trees are identical.")
    else:
        print("Trees are not identical.")
        
    # Test 2: Non-empty and non-identical trees:
    root1 = newNode(5)
    root2 = newNode(5)
    
    root1.left = newNode(3)
    root1.right = newNode(8)
    root1.left.left = newNode(2)
    root1.left.right = newNode(5)
  
    root2.left = newNode(3)
    root2.right = newNode(8)
    root2.left.left = newNode(2)
    root2.left.right = newNode(4)
  
    if (is_identical(root1, root2)):
        print("Trees are identical.")
    else:
        print("Trees are not identical.")
        
    # Test 3: Empty trees
    root1 = newNode(None)
    root2 = newNode(None)
    
    if (is_identical(root1, root2)):
        print("Trees are identical.")
    else:
        print("Trees are not identical.")
        
    # Test 4: One tree empty, the other one non-empty single node
    root1 = newNode(None)
    root2 = newNode(2)
    
    if (is_identical(root1, root2)):
        print("Trees are identical.")
    else:
        print("Trees are not identical.")

if __name__ == '__main__':
    main()