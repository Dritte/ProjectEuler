hashy = {}
max_length = 0
max_num = 0
def collatz_length(n):
    if n == 1:
        return 1
    if n in hashy:
        return hashy[n]
    if n%2 == 0:
        num = 1 + collatz_length(n/2)
    else:
        num = 1 + collatz_length(3*n+1)
    hashy[n] = num
    return num

for i in xrange(2, 1000000):
    if collatz_length(i) > max_length:
        max_length = collatz_length(i)
        max_num = i
print max_length


