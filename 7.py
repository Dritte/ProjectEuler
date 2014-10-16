primes = [2]
cur = 3
while len(primes) < 10001:
    print len(primes)
    if all([cur % prime != 0 for prime in primes]):
        primes.append(cur)
    cur += 1
print max(primes)
