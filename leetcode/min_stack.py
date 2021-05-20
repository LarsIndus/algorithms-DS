"""
Leetcode Problem 155: Min Stack (Easy)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    - push(x) -- Push element x onto stack.
    - pop() -- Removes the element on top of the stack.
    - top() -- Get the top element.
    - getMin() -- Retrieve the minimum element in the stack.

Source: https://www.youtube.com/watch?v=2wqSq2Lde-Q
"""

# Every time we push, we update the current minimum value.
# Similarly, every time we pop, we update the minimum value
# by traversing through the remaining elements.
# This way, the get_min() method can return the minimum in constant time.

class Min_Stack():
    
    def __init__(self):
        self.s = []
        self.min_val = float("inf")
        
    def push(self, x):
        self.s.append(x)
        if x < self.min_val:
            self.min_val = x
            
    def update_min(self):
        new_min = float("inf")
        for item in self.s:
            if item < new_min:
                new_min = item
        self.min_val = new_min
        
    def pop(self):
        if len(self.s) == 0: return None
        item = self.s.pop()
        if item == self.min_val:
            self.update_min()
        return item

    def top(self):
        if len(self.s) == 0: return None
        return self.s[-1]
    
    def get_min(self):
        return self.min_val

# Testing --------------------------------------------------------------------
def main():
    obj = Min_Stack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print("Element on top: ", obj.top(), sep = "")
    print("Popped the following: ", obj.pop(), sep = "")
    print("Now on top: ", obj.top(), sep = "")
    print("Current min: ", obj.get_min(), sep = "")
    obj.push(-1)
    print("Current min: ", obj.get_min(), sep = "")



if __name__ == '__main__':
    main()
