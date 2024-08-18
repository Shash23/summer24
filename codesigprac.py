def solution(numbers):
    
    sol = []
    
    for i in range(0, len(numbers) - 2):
        
        if ((numbers[i] < numbers[i+1] > numbers[i+2]) or (numbers[i] > numbers[i+1] < numbers[i+2])):
            sol.append(1)
            
        else:
            sol.append(0)
            
    return sol