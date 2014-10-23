def is_p(s): return all([s[i] == s[-i-1] for i in xrange(len(s)/2)])
print sum([i for i in xrange(10**6) if is_p(str(i)) and is_p(format(i,'b'))])
