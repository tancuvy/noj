#素数累加求和
a_range = range(100,201)
sum = 0
for i in a_range:
    flag = True
    for j in range (2,i): #判断素数！
        if i%j == 0: #能被其他的因数整除的就都不是素数
            flag = False
        else:
            continue
    if flag == True:
        sum = sum+i
print(sum)