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

n = 8
listy = []
while len(listy) < 11:
    if is_prime(n):
        c = n
        while c > 0:
            c/=10
            if not is_prime(c):
                break
        if c == 0:
            c = n
            while c > 0:
                c%=int(math.pow(10, int(math.log(c,10))))
                if not is_prime(c):
                    break
            if c == 0:
                listy.append(n)
    n+=1
print sum(listy)
