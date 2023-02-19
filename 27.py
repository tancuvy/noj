# 神奇的计算 一共乘法 共xyzmn 5 个元素
# xy*zmn = xmy*zn
count = 0
list = ['1','2','3','4','5','6','7','8','9']
for x in list:
    for y in list:
        for z in list:
            for m in list:
                for n in list:
                    if x!=y and x!=z and x!=m and x!=n and y!=z and y!=m and y!=n and z!=m and z!=n and m!=n: #当彼此都不相等时 才有可能成立
                        num1 = x+y
                        num2 = z+m+n
                        num3 = x+m+y
                        num4 = z+n
                        if int(num1)*int(num2) == int(num3)*int(num4): #换成数字 验证公式
                            count+=1
                        else:
                            continue
                    else:
                        continue

