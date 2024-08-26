from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')

        for i in nums:

            if i < first:
                first = i
            
            elif i < second:
                second = i

            elif i > second:
                print(first, second, i)
                return True

        return False
    
sol = Solution()
    
nums = [2, 4, -2, -3]
print(sol.increasingTriplet(nums))