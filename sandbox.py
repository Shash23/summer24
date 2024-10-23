arr = [1,2,4,7,8,2,3,4]
print(max(arr))
    

B = []

def h(A):
    if len(A) > 0:
        h(A[1:])
        B.append(A[0])
        
h([2, 5, 6, 3])

print(B)