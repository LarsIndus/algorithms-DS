def is_power(x, y):
    
    if y == 1:
        print("True: ", y, " = ", x, "^0", sep = "")
        return True
    elif x == 1:
        print("False")
        return False
    elif y < x:
        print("False")
        return False
    else:
        pow = 1
        while x ** pow <= y:
            if x ** pow == y:
                print("True: ", y, " = ", x, "^", pow, sep = "")
                return True
            pow += 1
        return False

is_power(5, 1)
is_power(1, 1)
is_power(1, 5)
is_power(5, 5)
is_power(5, 3)
is_power(5, 25)
is_power(19, 19 ** 15)


# Shorter solution:

def is_power_short(x, y):

    # The only power of 1 is 1 itself 
    if (x == 1):
        print(y == 1)
        return (y == 1)
  
    # Repeatedly comput power of x 
    pow = 1
    while (pow < y):
        pow *= x 
  
    # Check if power of x becomes y
    print(pow == y)
    return (pow == y)

is_power_short(5, 1)
is_power_short(1, 1)
is_power_short(1, 5)
is_power_short(5, 5)
is_power_short(5, 3)
is_power_short(5, 25)
is_power_short(19, 19 ** 15)           
            
        