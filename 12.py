import operator
#code for calculating number of divisors from
#https://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number
#will rewrite by self next time it comes up, its the products of all the (powers+1) of the prime factors of a number

# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)
        
def nth_triangular_number(n):
    return n*(n+1)/2

n = 1
while NumberOfDivisors(nth_triangular_number(n)) < 500:
    n+=1
print nth_triangular_number(n)
