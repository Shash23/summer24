from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

def threeSum(nums: List[int]) -> List[List[int]]:

        # take out a number and look in the array,
        # if there are two numbers that add up to that number but negative then that is valid

        # remember think about duplicate
        
        answer = []
        
        for i in nums:
            
            new_list = [element for element in nums if element != i]
            
            target = i * -1
            
            # check implementation
            result = twoSum(new_list, target)
            
            if(result != []):
                
                # order the elements
                temp = sorted([i, result[0], result[1]])
                
                if(temp not in answer):
                    
                    answer.append(temp)
                
        return answer        
            
nums = [0,1,1]
print(threeSum(nums))

nums = [0,0,0]
print(threeSum(nums))