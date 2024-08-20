from typing import List

def numPairsDivisibleBy60(time: List[int]) -> int:
    
    remainders = {} # (complement, occurences)
    ans = 0
    
    for i in time:
        
        rem = i % 60
        complement = (60 - rem) % 60
        
        if complement in remainders:
            ans += remainders[complement]
            
        remainders[rem] = 1 + remainders.get(rem, 0)
        
    
    return ans

time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))