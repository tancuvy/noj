# 水仙花
for n in range(100,1000):
    i = n // 100 #取百位数字 对一百整除
    j = n // 10 % 10 #取十位的数字 对10整除再对10取余
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)