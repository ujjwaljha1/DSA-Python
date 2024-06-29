# Palindrome number

def ispal(n):
    rev = 0
    temp = n
    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    if (rev == n):
        print(True)
    else:
        print(False)


x = int(input("Enter a number: "))
ispal(x)