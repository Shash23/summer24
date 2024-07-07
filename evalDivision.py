from typing import List
from collections import defaultdict

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

    def dfs(dividend, divisor, prod, visited):
        
        visited.add(dividend)
        ans = -1
        neighbors = graph[dividend]
        
        if(divisor in neighbors):
            ans = prod * neighbors[divisor]
        else:
            for neighbor, value in neighbors.items():
                if neighbor in visited:
                    continue
                ans = dfs(neighbor, divisor, prod * value, visited)
                if ans != -1:
                    break
        visited.remove(dividend)
        return ans
        


    graph = defaultdict(dict)

    # create the graph
    for (dividend, divisor), value in zip(equations, values):
        
        graph[dividend][divisor] = value
        graph[divisor][dividend] = 1 / value
        
    
    # now find if the path exists
    results = []
    
    for (dividend, divisor) in queries:
        
        if dividend not in graph or divisor not in graph:
            
            ans = -1
            
        elif dividend == divisor:
            
            ans = 1
            
        else:
            
            visited = set()
            ans = dfs(dividend, divisor, 1, visited)
            
            
        results.append(ans)
        
    return results
    
        
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        
print(calcEquation(equations, values, queries))


    
    