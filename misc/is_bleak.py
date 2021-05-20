# A simple Python 3 program  
# to check Bleak Number 
  
# Function to get no of set bits in binary  representation of passed  binary no.  
def countSetBits(x) : 
      
    count = 0
      
    while (x) : 
        x = x & (x - 1) 
        count = count + 1
      
    return count 
      
def isBleak(n) : 
  
    # Check for all numbers 'x' smaller than n.
    # If x + countSetBits(x) becomes n, then n can't be bleak. 
    for x in range(1, n) : 
          
        if (x + countSetBits(x) == n) : 
            return False
              
    return True
      
# Testing --------------------------------------------------------------------
def main():
    nums = [3, 4, 5, 10]
    for n in nums:
        if (isBleak(n)) : 
            print(n, " is bleak.", sep = "") 
        else : 
            print(n, " is not bleak.", sep = "")

if __name__ == '__main__':
    main()