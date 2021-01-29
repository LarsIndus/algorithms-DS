"""
Leetcode problem 100:

Check whether two binary trees are equal.
Time complexity of the below solution is O(n + m),
 with n and m denoting the number of the nodes of each tree.

Source: https://www.geeksforgeeks.org/check-whether-the-two-binary-search-trees-are-identical-or-not/
(code slightly adjusted)
"""
  
# Node implementation ------------------------------------------------------------------
class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, data):  
        self.data = data 
        self.left = None
        self.right = None

# Solution ----------------------------------------------------------------------------
def is_identical(root1, root2):
  
    if root1 is None and root2 is None: return True
    if root1 is None or root2 is None: return False
    if root1.data != root2.data: return False
    
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)
      
# Testing ---------------------------------------------------------------------------- 
if __name__ == '__main__':
      
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