def pentagonal_number(n):
    return n*(3*n-1)/2
hashy = {}
for i in xrange(1,1000000):
    hashy[pentagonal_number(i)] = True
nums = sorted(hashy.keys())
def answer():
    for x in nums:
        for y in nums:
            if y >= x:
                break
            if x - y in hashy and x + y in hashy:
                return x-y
print answer()
