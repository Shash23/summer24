def can_reduce_to_zero(arr, x, y, k):
    required_ops = 0
    for element in arr:
        if element <= k * y:
            continue
        extra_ops = (element - k * y + x - y - 1) // (x - y)
        required_ops += extra_ops
        if required_ops > k:
            return False
    return True

def min_operations_to_zero(arr, x, y):
    left, right = 0, max(arr) // min(x, y) + 1
    while left < right:
        mid = (left + right) // 2
        if can_reduce_to_zero(arr, x, y, mid):
            right = mid
        else:
            left = mid + 1
    return left

executionTime=[3,3,6,3,9]
x, y = 3, 2

print(min_operations_to_zero(executionTime, x, y))