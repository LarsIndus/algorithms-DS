# This function returns the first reoccurring character in a given string.
# If all characters are unique, it returns None.
def first_reoccurring(string):
    
    # Use a set as searching in a set is more efficient than in a list (?)
    # Note that, iterating over the elements is more efficient for lists, though.
    chars = set()
    
    for char in string:
        if char in chars: return char
        chars.add(char)
        
    return None


# This function returns the first non-reoccurring character in a string.
# If all characters reoccur, it returns None.
def first_non_reoccurring(string):
    
    unique_chars = []
    counts = {}
    
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1 
            unique_chars.append(char)
            
    for char in unique_chars:
        if counts[char] == 1:
            return char
        
    return None