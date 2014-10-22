def factorial(n):
    if n==1 or n == 0:
        return 1
    return n*factorial(n-1)

s = 0
for num in xrange(3,100000):
    copy = num
    sumy = 0
    while copy>0:
        sumy+=factorial(copy%10)
        copy/=10
    if sumy == num:
        s+=sumy
print s
    
