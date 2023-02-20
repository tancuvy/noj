# 合并区间
n = int(input()) # 多少组区间
a = input() # 每个区间的数
a_list = [int(i) for i in a.split(' ')] #保存成列表
b_list = []
i = 0
while i < len(a_list): # 把区间分好 两两一组
    c_list = []
    c_list.append(a_list[i])
    c_list.append(a_list[i + 1])
    i = i + 2
    b_list.append(c_list)
print(b_list)
b_list.sort() # 对每组进行排序 区间开头小的放前面 ！直接确定每组最小值的位置！关键！
print(b_list)
i = 0
while i < len(b_list) - 1: # len(b_list)是多少组区间 但凡还有两组都要进行合并
    m = b_list[i] # 理解成左边的组
    n = b_list[i + 1] # 右边的组
    if m[1] < n[0] : # 左组最大值<右组最小值 不用合并
        i = i + 1
    else: # 左组最大值>右组最小值 需要合并
        b_list[i][1] = max(n[1],m[1]) # 确定合并后组的最大值
        del b_list[i + 1]
        continue
for i in b_list:
    print(i[0],i[1],end=' ')