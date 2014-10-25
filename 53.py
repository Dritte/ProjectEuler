factorial = [1]
for i in xrange(1, 101):
    factorial.append(factorial[-1]*i)
def choose(n, r):
    if n < r:
        raise
    return factorial[n] / factorial[r] / factorial[n-r]
sumy=0
for n in xrange(1,101):
    for r in xrange(1, n):
        if choose(n, r) > 10**6:
            sumy+=1
print sumy
