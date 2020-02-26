import math

def is_perfect(n):
    
    if n > 1:
        i = 2
        sum_of_divisors = 1
        while i <= math.sqrt(n):
            if n % i == 0:
                sum_of_divisors += i
                sum_of_divisors += n / i
            i += 1
            
        return sum_of_divisors == n
    
    return False

# This function also outputs the divisors
def is_perfect_print(n):
    
    if n > 1:
        i = 2
        divisors = [1]
        while i <= math.sqrt(n):
            if n % i == 0:
                divisors.append(i)
                divisors.append(n // i)
            i += 1
            
        if sum(divisors) == n:
            divisors.sort()
            return divisors
    
    print(n, "is not a perfect number.")