def isSorted(l):
    i = 1

    while i < len(l):

        if l[i] < l[i - 1]:
            return False
        i = i + 1

    return True


l = [10, 20, 30, 15, 40]

if isSorted(l):
    print("Yes")
else:
    print("No")