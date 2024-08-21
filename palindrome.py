def palindrome(x: int):
    
    tmp = str(x)
    
    if tmp == tmp[::-1]:
        return True
    
    else:
        return False