import itertools
dim = 9
hashy={}
for num in itertools.permutations(range(1,dim+1)):
    for mult_pos in xrange(1,dim-1):
        for eq_pos in xrange(mult_pos+1,dim):
            n1=0
            n2=0
            n3=0
            for d in num[:mult_pos]:
                n1*=10
                n1+=d
            for d in num[mult_pos:eq_pos]:
                n2*=10
                n2+=d
            for d in num[eq_pos:]:
                n3*=10
                n3+=d
            if n1*n2 == n3:
                hashy[n3] = True
print sum(hashy.keys())
