#数字规律相加
# n = 1     1
# n = 2     1 + 12
# n = 3     1 + 12 + 112
# n = 4     1 + 12 + 112 + 1112
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(13)
else:
    temp = 12
    tempsum = 13
    for i in range (0,n-2): #一共n次相加 少了上面两次 变成n-2次
        temp = (temp-1)*10+2
        tempsum += temp
    print(tempsum)