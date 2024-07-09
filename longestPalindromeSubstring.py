def longestPalindrome(self, s: str) -> str:
    
    lp = len(s) // 2
    rp = lp + 1
    
    if(len(s) == 1 or s is None):
        return s
    
    
    