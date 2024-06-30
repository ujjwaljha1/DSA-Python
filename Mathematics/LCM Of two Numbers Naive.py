# GCD and HCF of two numbers
# naive

def lcm(a, b):
    res = max(a, b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1
    return res


a = 12
b = 15
print(lcm(a, b))