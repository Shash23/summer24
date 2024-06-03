# def checkPos(a: List[int], b: List) -> 
from typing import List

def checkTarget(target: int, new_pos: List[int], speed: List[int]):
    
    for i in range(len(new_pos) -1, -1, -1):
        
        if new_pos[i] == target:
            del new_pos[i]
            del speed[i]
            
    return new_pos, speed



def carFleet(target: int, position: List[int], speed: List[int]) -> int:

        # base case
        if len(position) == 1:
            return 1

        fleets = 0

        flag = True
        
        new_pos = position.copy()
        
        while flag:
            
            if len(new_pos) == 0:
                break
            
            # remove all occurences of the target
            # issue here is that the corresponding elements in speed must be taken out
            new_pos = [pos + spd for pos, spd in zip(new_pos, speed)]
            
            if(target in new_pos):
                
                new_pos = [element for element in new_pos if element != target]
                fleets += 1
            
            if not new_pos:
                flag = False
            
        return fleets


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

result = carFleet(target, position, speed)
print(result)