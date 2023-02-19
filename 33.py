# lambda函数是一种匿名函数，即没有名字的函数
# 使用lambda保留字定义，函数名是返回结果
# lambda函数的函数体只是一个表达式
# lambda函数用于定义简单的、能够在一行内表示的函数
a = input()
m,n=[int(i) for i in a.split(" ")]
b = input()
b_list = [int(i) for i in b.split(' ')]

res = sorted(b_list,key = lambda x:abs(x-n)) #排序 规则是 按照每个数字与n的距离 
for i in res:
    print(i,end=" ")