import fractions 
global_num = 1
global_den = 1
for num in xrange(10,101):
    for den in xrange(num+1, 101):
        if den%10!=0:
            if fractions.Fraction(num, den) == fractions.Fraction(num/10, den%10) and num%10 == den/10:
                global_num*=num
                global_den*=den
print fractions.Fraction(global_num, global_den)

