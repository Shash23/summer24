def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
            
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i in range(len(nums)):

            temp = target - nums[i]

            if temp in hash_map:
                return [i, hash_map[temp]]

            hash_map[nums[i]] = i

            


        
        