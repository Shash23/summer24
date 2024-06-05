from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    
    idx = [element for element in range(len(temperatures))]
    temp_idx = [[temp, idx] for temp, idx in zip(temperatures, idx)]
    
    # [73, 0], [74, 1], [75, 2], [71, 3], [69, 4], [72, 5], [76, 6], [73, 7]
    
    n = len(temperatures)
    ans = [0] * n
    
    stack = []
    
    for temp in temp_idx:
        
        while stack and temp[0] > stack[-1][0]:
            
            popped = stack.pop()
            ans_idx = popped[1]    
            ans[ans_idx] = temp[1] - popped[1]
            
        stack.append(temp)
    
    return ans
        
temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
        
        
    
    
        
        