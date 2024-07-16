def getDistinctGoodnessValues(arr):
    n = len(arr)
    dp = [0] * 1024
    dp[0] = 1

    for i in range(n):
        new_dp = [0] * 1024
        for j in range(1024):
            new_dp[j | arr[i]] |= dp[j]
        dp = new_dp

    goodness_values = [i for i in range(1024) if dp[i]]
    return sorted(goodness_values)

n = 4
arr = [4, 2, 4, 1]
print(getDistinctGoodnessValues(arr))