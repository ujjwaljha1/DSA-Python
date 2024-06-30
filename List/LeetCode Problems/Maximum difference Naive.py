# Maximum Difference
# Naive

def maxdiff(arr, n):
    res = arr[1] - arr[0]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            res = max(res, arr[j] - arr[i])

    return res


arr = [2, 3, 10, 6, 4, 8, 1]
n = len(arr)
print(maxdiff(arr, n))