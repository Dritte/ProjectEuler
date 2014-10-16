hashy = {}
num = 2000000
for i in xrange(2, num):
    hashy[i] = True
p = 2
while p < num:
    if p in hashy:
        cur = 2*p
        while cur < num:
            if cur in hashy:
                del hashy[cur]
            cur += p
    p+=1
print sum(hashy.keys())
