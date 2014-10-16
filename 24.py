import itertools
listy=[]
for p in itertools.permutations("0123456789"):
    print len(listy)
    num = 0
    for n in p:
        num*=10
        num+=int(n)
    listy.append(num)
print sorted(listy)[1000000-1]
