class Solution:

    # return the index its at
    def binary_search(self, target, nums) -> int:

        left = 0
        right = len(nums) - 1

        if not nums:

            return -1

        while (left <= right):

            mid = (left + right) // 2

            if nums[mid] == target:

                return mid
                
            elif target > nums[mid]:
                left = mid + 1
            
            else:
                right = mid - 1

        return -1
    
    def longestSquareStreak(self, nums: List[int]) -> int:

        max_streak = 0
        nums.sort()
        
        for i in range(len(nums)):
            
            temp = nums[i]
            temp_streak = 1

            while self.binary_search(temp * temp, nums) != -1:
                temp = temp * temp
                temp_streak += 1

            
            max_streak = max(max_streak, temp_streak)

        return max_streak if max_streak > 1 else -1
