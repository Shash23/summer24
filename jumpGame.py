class Solution:
    def canJump(self, nums: List[int]) -> bool:


        i = 0
        farthest_point = 0

        while i < len(nums) and i <= farthest_point:

            farthest_point = max(farthest_point, i + nums[i])
            i += 1

        return i == len(nums)