#反转元组
num = input()
num_list = [int(i) for i in num.split(" ")]#先输入成一个列表
resverse_list = num_list[::-1] #列表反转
res = [num_list[i]+resverse_list[i] for i in range (len(num_list))] #列表1,2相加
print(tuple(res)) #最后转成元组