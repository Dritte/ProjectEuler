print max([x*y for x in xrange(1000) for y in xrange(1000) if all([str(x*y)[i] == str(x*y)[-(i + 1)] for i in xrange(len(str(x*y)))])])
