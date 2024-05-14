
def climbingStairs(self, n:int) -> int:
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    dp = [0] * n
    dp[n-1] = 1
    dp[n-2] = 2
    
    # range(start, stop, step)
    for i in range(n - 3, -1, -1):
        
        dp[i] = dp[i+1] + dp[i+2]
        
    return dp[0]


        
        
        
        
        
        
        
        
        
        
        
    
    