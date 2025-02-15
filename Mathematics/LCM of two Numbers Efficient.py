# GCD and HCF of two numbers
# Efficient

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


a = 12
b = 15
print(lcm(a, b))



