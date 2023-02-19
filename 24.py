# 列表不相邻整数的最大和
n = input()
list = [int(i) for i in n.split(" ")]
max = 0
for i in range (len(list)):
    for j in range (i+2,len(list)):
        if list[i]+list[j]>max:
            max = list[i]+list[j]
print(max)
