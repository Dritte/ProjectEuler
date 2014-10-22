sumy = -1
for d9 in xrange(10):
    for d0 in xrange(10):
        for d1 in xrange(10):
            for d2 in xrange(10):
                for d3 in xrange(10):
                    for d4 in xrange(10):
                        if d9*10**5 + d0*10**4 + d1*10**3 + d2*10**2 + d3*10**1 + d4 * 10**0 == d9**5 + d0**5 + d1**5 + d2**5 + d3**5 + d4 **5:
                            sumy+=d9*10**5 + d0*10**4 + d1*10**3 + d2*10**2 + d3*10**1 + d4 * 10**0
print sumy
