num = 100
print sum([x+1 for x in xrange(num)])**2 - sum([(x+1)**2 for x in xrange(num)])
