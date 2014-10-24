def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
upper_bound = 1000000
primes = [x for x in xrange(2, upper_bound/2 + 1) if is_prime(x)]
maxy_len = 0
maxy_num = 0
for i in xrange(len(primes)-2):
    for j in xrange(i+maxy_len, len(primes)):
        num = sum(primes[i:j])
        if num > upper_bound:
            break
        if j-i > maxy_len:
            if is_prime(num):
                maxy_len = j-i
                maxy_num = num
print maxy_num
