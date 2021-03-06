import math
#using the python primality test from wikipedia
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
#I really should've not made this a one-liner.
print sum([all([is_prime(int(str(x)[i:])*10**i + int(str(x)[:i])) for i in xrange(1,len(str(x)))] + [is_prime(x)]) for x in xrange(1000001)])
