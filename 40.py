s = "".join([str(x) for x in xrange(1,1000000)])
print reduce(lambda x, y: x*y, [int(s[10**i-1]) for i in xrange(7)], 1)
