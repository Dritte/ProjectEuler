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

max_n = 0
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        n=0
        while is_prime(n**2 + a*n + b):
            n+=1
        if n > max_n:
            max_n = n
            print n
            print a*b
