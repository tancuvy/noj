#计算今年多少天 是不是闰年
day = int(input())
if day % 4 == 0 and day % 100 != 0:
    print('366')
elif day % 100 == 0 and day % 400 == 0:
    print('366')
else:
    print('365')