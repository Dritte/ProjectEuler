hashy={}
hashy[0]=0
hashy[1]=3
hashy[2]=3
hashy[3]=5
hashy[4]=4
hashy[5]=4
hashy[6]=3
hashy[7]=5
hashy[8]=5
hashy[9]=4
hashy[10]=3
hashy[11]=6
hashy[12]=6
hashy[13]=8
hashy[14]=8
hashy[15]=7
hashy[16]=7
hashy[17]=9
hashy[18]=8
hashy[19]=8
hashy[20]=6
hashy[30]=6
hashy[40]=5
hashy[50]=5
hashy[60]=5
hashy[70]=7
hashy[80]=6
hashy[90]=6
def calc(i):
    if i in hashy:
        return i
    sumy = 0
    if i%100 in hashy:
        sumy+= hashy[i%100]
    else:
       sumy+=hashy[((i/10)%10)*10]
       sumy+=hashy[i%10]
    if i >= 100:
        sumy+= hashy[i/100] + 7
        if i%100 != 0:
            sumy+=3
    hashy[i] = sumy
for i in xrange(1, 1000):
    if i not in hashy:
        calc(i)
print sum(hashy.values()) + 3 + 8
