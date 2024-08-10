class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
    
    
def counting(s: str, t: str) -> bool:
        
    dict_1 = {}
        
    for i in s:
            
        if i not in dict_1.keys():
            dict_1[i] = 1
            
        else: 
            dict_1[i] += 1
            
    # print(dict_1)
    
    dict_2 = {}
        
    for i in t:
            
        if i not in dict_2.keys():
            dict_2[i] = 1
            
        else: 
            dict_2[i] += 1
        
    return dict_1 == dict_2
        
print(counting("anagram", "nagaram"))
