import itertools
pan = itertools.permutations("123456789")
hashy = {}
for p in pan:
    hashy[p] = True
m = 0
for i in xrange(1,1000000):
    prod = 1
    x = 2
    while prod<10000000000:
        s = ""
        for p in xrange(1, x+1):
            s+=str(i*p)
        prod = int(s)
        listy = []
        copy = prod
        while copy > 0:
            listy.append(str(copy%10))
            copy/=10
        listy.reverse()
        if tuple(listy) in hashy:
            if prod > m:
                m = prod
        x+=1
print m
