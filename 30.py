# 长城最长凸起 就是找极值点 并且寻找“山”的长度 最少的极值长度是3 ： 1 3 2
heigth = input()
list = [int(i) for i in heigth.split(" ")]
maxnum = 0
count = [0] * len(list) #表示 最终结果的长度 山的长度 若i的位置是2 也就是该点左右两侧两个位置都符合规则 最后长度就是2*2+1 = 5
for i in range(1, len(list) - 1): #从第二个数开始找
    if list[i] > list[i - 1] and list[i] > list[i + 1]: #若比前一个数字和后一个数字大 就是最小的极值点
        print('i=', i)
        print('len(list)-2', len(list) - 2)
        count[i] += 1 #此时极值点存在 i的位置保存极值点的位置
        print(count)
        if i < len(list) - 2 and i > 1: # 如果这个极值点 比较靠边 左或右只有一个数 那么该极值点“山”的长度就是3 若不是则 山的长度大于3
            for k in range(1, min(i, len(list) - i - 1)):
                #看极值点 旁边还有几个数字 2 1 4 7 3 2 比如7左边有三个 但是右边只有两个 那么再比较它旁边的数是否符合规则的次数就是2-1次
                print('min', min(i, len(list) - i - 1))
                print(k)
                if list[i - k] > list[i - (k + 1)] and list[i + k] > list[i + (k + 1)]:
                    #比较极值左右相邻的两个数字 是不是符合规则 也就是 4是不是比1大 3是不是比2大
                    print(list[i - k], list[i - (k + 1)], list[i + k], list[i + (k + 1)])
                    count[i] += 1 #如果符合规则
                    print(count)
        elif i == len(list) - 2 or i == 1:#此极值点山的长度是3
            continue
        else:
            count[i] = 0 #没有极值点
maxnum = count[0]
for i in range(1, len(count)):
    if maxnum < count[i]:
        maxnum = count[i] #找count中的最大数
if maxnum > 0:
    print((maxnum * 2) + 1)
else:
    print(maxnum)