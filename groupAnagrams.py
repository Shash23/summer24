from typing import List
import collections

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    res = collections.defaultdict()
    
    for i in strs:
        
        res[tuple(sorted(i))].append(i)
        
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))