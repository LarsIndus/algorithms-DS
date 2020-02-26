# A simple Python 3 program  
# to check Bleak Number 
  
# Function to get no of set bits in binary  representation of passed  binary no.  
def countSetBits(x) : 
      
    count = 0
      
    while (x) : 
        x = x & (x-1) 
        count = count + 1
      
    return count 
      
# Returns true if n 
# is Bleak 
def isBleak(n) : 
  
    # Check for all numbers 'x' 
    # smaller than n. If x +  
    # countSetBits(x) becomes 
    # n, then n can't be Bleak. 
    for x in range(1, n) : 
          
        if (x + countSetBits(x) == n) : 
            return False
              
    return True
      
# Driver code 
if(isBleak(3)) : 
    print( "Yes") 
else : 
    print("No") 
  
if(isBleak(4)) : 
    print("Yes") 
else :  
    print( "No") 