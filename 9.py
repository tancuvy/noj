#判断数字的二进制是否全为1
N = int(input())
List = []
for i in range(N):
    number = str('{:b}'.format(int(input()))) #直接把10进制数字变成2进制的字符串
    number = list(number) #变为字符串列表
    for index, item in enumerate(number):
        number[index] = int(item) #变为数字列表
    if all(number) :#all函数的参数（元素除了是 0、空、None、False）外都算True，有一个FALSE就是false，都是TRUE才是true
        List.append( ' True ' ) #二进制非0 即1
    else:
        List.append( ' False' )
for index, item in enumerate(List) :
    if index+1 < N:
        print(item,end=',')
    else:
        print(item,end=' ')

