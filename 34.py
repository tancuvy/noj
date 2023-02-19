# 发水果 第一轮 第一个人一个 第二个人两个 。。。。。
#       第二轮 第一个人 n+1个 第二个人n+2个 。。。
# 相当于无数个人 第一个人发1个 ......第n+1个人发 n+1个
# 不够了就当前人剩下的所有
a = input()
n,m = [int(i) for i in a.split(" ")] #n孩子的个数 m是水果数量
list = [0]*n #列表有n个0，小孩的数量
dispatch = 1
while m > 0: #当水果还有就要发 也就控制轮数 因为dispatch一直都相加 第一轮结束 dispatch也就是n+1 第二轮第一个人直接就发5个
    for i in range(len(list)): #从第一个孩子开始发
        list[i] += min(m, dispatch) #发 min 的水果
        m -= dispatch #水果数量更新
        if m == 0: #水果发完了
            break;
        dispatch += 1
for i in list:
    print(i,end=" ")