n=int(input("Enter a number: "))
res=0
while n>0:
    n=n//10
    res+=1
print(res)