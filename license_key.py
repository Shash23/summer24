class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.replace('-','')
        s = s.upper()

        N = len(s) % k 
        
        parts = []

        if N > 0:

            parts.append(s[:N])
        
        for i in range(N, len(s), k):
            
            parts.append(s[i:i+k])
            
        return '-'.join(parts)
        