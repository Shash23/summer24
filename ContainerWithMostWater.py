from typing import List

def maxArea(height: List[int]) -> int:

    # use two pointers, one starting from the end, and one starting from the beginning

    start = 0
    end = len(height) - 1
    
    area = 0
    
    while start < end:
        
        width = end - start
        
        temp_area = width * min(height[start], height[end])
        
        area = max(temp_area, area)
        
        if(height[end] < height[start]):
            
            end -= 1
            
        else:
            
            start += 1
    
    return area

#height = [1,8,6,2,5,4,8,3,7]
height = [1,2,4,3]
print(maxArea(height))

        
        
        
        