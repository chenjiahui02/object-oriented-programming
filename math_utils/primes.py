from math import sqrt


def isprime(n):
    if n == 2 or n == 3:
        return True
    elif n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
            return True
