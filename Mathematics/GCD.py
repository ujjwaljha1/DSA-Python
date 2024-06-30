# GCD and HCF of two numbers
#Euclidean Algorithim

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(gcd(a, b))