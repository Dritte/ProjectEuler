def d(n):
    sumy=0
    for d in xrange(1,n):
        if n % d == 0:
            sumy+=d
    return sumy
print sum([n for n in xrange(1,10000) if d(d(n)) == n and n!=d(n)])
