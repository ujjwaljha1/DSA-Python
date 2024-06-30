def countOccurr(l,x):
    cnt = 0

    for e in l:
        if e==x:
            cnt+=1

    return cnt

l = [10,20,20,20,30,30]

print(10,countOccurr(l, 10))
print(20,countOccurr(l, 20))
print(30,countOccurr(l, 30))
print(25,countOccurr(l, 25))