def firstOccurence(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


n = 5
arr = [5, 10, 10, 15, 15]
x = 15
print(firstOccurence(arr, n, x))