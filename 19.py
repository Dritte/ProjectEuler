non_leap_months = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_months = [31,29,31,30,31,30,31,31,30,31,30,31]
years = range(1900, 2001)
day=1
count = 0
for year in years:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months = leap_months
    else:
        months = non_leap_months
    for month in months:
        for d in xrange(month):
            if day == 0 and d == 0:
                if year > 1900:
                    count+=1
            day+=1
            day%=7
    print day
print count
