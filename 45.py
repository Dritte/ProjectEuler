def tri(n): return n*(n+1)/2
def pen(n): return n*(3*n-1)/2
def hexa(n): return n*(2*n-1)

x = 285 + 1
y = 165
z = 143

while tri(x)!=pen(y) and tri(x)!=hexa(z):
    if tri(x) < pen(y) or tri(x) < hexa(z):
        x+=1
    if pen(y) < tri(x) or pen(y) < hexa(z):
        y+=1
    if hexa(z) < pen(y) or hexa(z) < tri(x):
        z+=1
print tri(x)
