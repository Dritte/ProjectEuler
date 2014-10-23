max_p = 1
max_answers = 0
for p in xrange (1, 1001):
    answers = {}
    for a in xrange(p+1):
        for b in xrange(0, p-a+1):
            c = p - a - b
            if a**2 + b **2 == c **2:
                miny = min([a,b,c])
                maxy = max([a,b,c])
                midy = p - miny - maxy
                tuply = (miny, midy, maxy)
                if tuply not in answers and miny != 0:
                    answers[tuply] = True
    if len(answers.keys()) > max_answers:
        max_answers = len(answers.keys())
        max_p = p
print max_p
