class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        left = -1 # hasn't been seen yet
        ans = 0
        
        for right in range(len(seats)):
            
            if seats[right] == 1:
                
                # if empty at start
                if left == -1:
                    ans = right
                
                else:
                    ans = max(ans, (right - left) // 2)

                left = right

        # if empty at end
        if seats[-1] == 0:
            ans = max(ans, len(seats) - 1 - left)
            

        return ans