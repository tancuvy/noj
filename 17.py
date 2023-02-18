#找重复数字，计算出现的次数，用字典
num = input()
num_list = [int(i) for i in num.split(",")]
num_list.sort() #排序，好找。次数的列表就能指向数字
res = {} #字典，存数据
for i in num_list: #遍历列表中元素
    res[i] = num_list.count(i)
print(res)
