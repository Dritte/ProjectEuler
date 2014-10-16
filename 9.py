import math
print [a*b*math.sqrt(a**2+b**2) for a in xrange(1000) for b in xrange(1000-a) if math.sqrt(a**2+b**2)==int(math.sqrt(a**2+b**2)) and math.sqrt(a**2+b**2)+a+b == 1000]
