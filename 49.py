import math
import itertools
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
def tuple_to_int(t, length):
    n = 0
    for i in xrange(length):
        n*=10
        n+=t[i]
    return n
def answer():
    for it in itertools.permutations(range(0,10)*4,4):
        hashy = {}
        for i in itertools.permutations(it):
            if tuple_to_int(i,4)>999 and is_prime(tuple_to_int(i,4)):
                hashy[tuple_to_int(i,4)] = True
        for i in hashy.keys():
            for j in hashy.keys():
                if i<j:
                    if 2*j - i in hashy:
                        if i!= 1487:
                            return str(i)+str(j)+str(2*j-i)
print answer()
