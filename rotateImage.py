def rotate(matrix: List[List[int]]) -> None:
    
    n = len(matrix)
    
    # remember to not overlap
    
    # transpose
    for i in range(n):
        for j in range(i+1, n):
            
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # reflect
    
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][j - 1] = (matrix[i][-j-1], matrix[i][j],)
    
    
    for i in range(n):
        matrix[i].reverse()
