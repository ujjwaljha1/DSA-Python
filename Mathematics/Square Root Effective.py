def sqrootfloor(n):
    low = 1
    high = n
    ans = -1
    while (low <= high):
        mid = (low + high) // 2
        msq = mid * mid
        if (msq == n):
            return mid
        elif (msq > n):
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans


n = 9
print(sqrootfloor(n))