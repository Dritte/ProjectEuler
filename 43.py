import itertools
sumy = 0
pan = itertools.permutations("".join([str(x) for x in xrange(0,10)]))
divisors = [2,3,5,7,11,13,17]
hashy = {}
for p in pan:
    hashy[p] = True
for key in hashy.keys():
    for i in xrange(7):
        key_num = 0 
        for digit in key[i+1:i+4]:
            key_num*=10
            key_num+=int(digit)
        if key_num % divisors[i] != 0:
            break
        if i == 6:
            key_num = 0
            for digit in key:
                key_num*=10
                key_num+=int(digit)
            sumy+=key_num
print sumy
