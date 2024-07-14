def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        return nums[len(nums) // 2]
    
    
    