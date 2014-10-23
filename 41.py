import itertools
import math
#using the python primality test from wikipedia
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

m = 0
for n in xrange(1,10):
    pan = itertools.permutations("".join([str(x) for x in xrange(1,n+1)]))
    hashy = {}
    for p in pan:
        hashy[p] = True
    for key in hashy.keys():
        key_num = 0
        for digit in key:
            key_num*=10
            key_num+=int(digit)
        if is_prime(key_num):
            if key_num > m:
                m = key_num
print m
