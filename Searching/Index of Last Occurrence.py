#Naive

def lastOccur(l,x):

    for i in reversed(range(len(l))):

        if l[i] == x:
            return i
    return -1

l = [10,15,20,20,40,40]

print(20,lastOccur(l, 20))
print(40,lastOccur(l, 40))
