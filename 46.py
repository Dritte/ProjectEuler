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
primes = [2]
n = 3
while n%2==0 or is_prime(n) or any([((n*1.0-prime*1.0)/2.0)**(1.0/2.0) == int(((n*1.0-prime*1.0)/2.0)**(1.0/2.0)) for prime in primes]):
    if is_prime(n):
        primes.append(n)
    n+=1
print n
