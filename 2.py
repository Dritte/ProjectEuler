x = 1
y = 2
z = x+y
sumy = 2
while z < 4000000:
    if z%2==0:
        sumy+=z
    x=y
    y=z
    z=x+y
print sumy
