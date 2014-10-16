num = 600851475143
divisor = 2
divisors = []
while not num == 1:
    if num % divisor == 0:
        num /= divisor
        divisors.append(divisor)
    else:
        divisor += 1
print max(divisors)
