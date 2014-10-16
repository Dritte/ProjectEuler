def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
s = str(factorial(100))
print sum([int(digit) for digit in s])
