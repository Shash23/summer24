from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
        
        # iterate through the array one pass

        # store each element with index in dictionary (value, index)

        # if the complement is in the dict, then put it in the answer with the current
        
        result = [0] * 2

        vals = {}

        for index, element in enumerate(numbers, start = 1):

            if(target - element in vals):
                result[0] = vals[target - element]
                result[1] = index
                return result
            else:
                vals[element] = index
                
        return result
                
numbers = [2,7,11,15]
target = 9
                
numbers = [2,3,4]
target = 6                

print(twoSum(numbers, target))
            



        