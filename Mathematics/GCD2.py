# GCD and HCF of two numbers

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(gcd(a, b))