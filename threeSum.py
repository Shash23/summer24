class Solution:

    def twoSum(nums: List[int], target:int) -> List[int]:

        hash_map = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hash_map:
                return [nums[i], temp]

            hash_map[temp] = i

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        target = 0
        result = []

        hash_map = {}
        nums.sort()
        

        for i in range(len(nums)):

            temp = target - nums[i]
            
            if temp in hash_map:
                return [i, hash_map[temp]]

            hash_map[nums[i]] = i