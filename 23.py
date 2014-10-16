def d(n):
    sumy=0
    for d in xrange(1,n):
        if n % d == 0:
            sumy+=d
    return sumy
hashy = {}
sumy = 0
for n in xrange(1, 28124):
    if d(n) > n:
        hashy[n] = True
for n in xrange(1, 28124):
    b = True
    for m in hashy.keys():
        if (n-m) in hashy:
            b = False
            break
    if b:
        sumy+=n
print sumy
