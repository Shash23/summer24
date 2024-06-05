# def checkPos(a: List[int], b: List) -> 
from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0

        cars = list(zip(position, speed))
        stack = []
        
        cars.sort(reverse=True)
        
        for pos, speed in cars:
            
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)

        


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

result = carFleet(target, position, speed)
print(result)


