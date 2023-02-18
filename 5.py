#判断几个字符串或数字是否是回文的
n = int(input())
list1 = []
res = []
for i in range (n):
    list1.append(input())

for temp in list1: #比较每个在list1中的数字
    flag = True
    pmet = temp[::-1] #把每个数字（字符串）前后颠倒
    for j in range (len(temp)):
        if pmet[j] != temp[j]:#按位比较
            flag = False
            res.append("False") #结果列表
            break
    if flag :
        res.append("True") #如果前后都一样，这个字符串就是回文的
l = len(res)
for k in range (l):
    if k == l-1 :
        print(res[k])
    else:
        print(res[k],end=",")


