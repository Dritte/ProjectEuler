def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
def get_factors(n):
    if is_prime(n):
        return False
    listy = []
    m = 2
    while n > 1:
        if len(listy)>4:
            return False
        if n%m==0:
            if len(listy) > 0 and listy[-1]%m==0:
                listy[-1]*=m
            else:
                listy.append(m)
            n/=m
        else:
            m+=1
    return len(listy)==4
n = 2
while not all([get_factors(x) for x in xrange(n, n+4)]):
    print n
    n+=1
print n
