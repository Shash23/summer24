from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, starting_node):
    
    queue = deque() # to track what to explore
    visited = set() # to track visited
    
    queue.append(starting_node)
    
    while queue:
        
        node = queue.popleft()
        visited.add(node)
        
        for neighbor in graph[node]:
            
            if neighbor not in visited:
                
                queue.append(neighbor)
                visited.add(neighbor)
                
    
    return visited    
    
print(bfs(graph, 'A'))