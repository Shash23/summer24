from collections import Counter

def firstUniqChar(s: str) -> int:
    
    count = Counter(s)
    
    for idx, ele in enumerate(s):
        
        if count[ele] == 1:
            
            return idx
        
    return -1