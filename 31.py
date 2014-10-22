sumy = 0
for a in xrange(201):
    for b in xrange(101):
        if a + 2*b > 200:
            break
        for c in xrange(41):
            if a + 2*b + 5*c > 200:
                break
            for d in xrange(21):
                if a + 2*b + 5*c + 10*d > 200:
                    break
                for e in xrange(11):
                    if a + 2*b + 5*c + 10*d + 20*e > 200:
                        break
                    for f in xrange(5):
                        if a + 2*b + 5*c + 10*d + 20*e + 50*f > 200:
                            break
                        for g in xrange(3):
                            for h in xrange(2):
                                if a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h == 200:
                                    sumy+=1
print sumy
