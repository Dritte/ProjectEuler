count = 3
a = 1
b = 1
c = a+b
ten_to_999 = 10**999
while c < ten_to_999:
    count += 1
    a = b
    b = c
    c = a + b
print count
