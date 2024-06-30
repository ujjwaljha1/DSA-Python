# Check for Prime
# naive

def isprime(n):
    if n == 1:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True


n = 7
print(isprime(n))
