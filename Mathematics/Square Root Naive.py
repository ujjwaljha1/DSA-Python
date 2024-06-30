def sqrootfloor(n):
    i=1
    while(i*i<=n):
        i+=1
    return i-1

n=9
print(sqrootfloor(n))