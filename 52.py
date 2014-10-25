def get_digits(n):
    hashy = {}
    while n > 0:
        if n%10 in hashy:
            hashy[n%10]+=1
        else:
            hashy[n%10]=1
        n/=10
    return hashy
def same_6_digits(n):
    digits_dict = get_digits(n)
    for multiple in xrange(2,7):
        multiple_dict = get_digits(multiple*n)
        if not len(digits_dict.keys()) == len(multiple_dict.keys()):
            return False
        for digit in digits_dict.keys():
            if digit not in multiple_dict:
                return False
            else:
                if not digits_dict[digit]==multiple_dict[digit]:
                    return False
    return True
n=1
while not same_6_digits(n):
    n+=1
print n
