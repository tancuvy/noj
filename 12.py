#内置函数
num = input()
num_list =[int(i) for i in num.split(' ')]
print(len(num_list),end=",")
print(max(num_list),end=",")
print(min(num_list),end=",")
print(sum(num_list))

for i in range (len(num_list)):
    if num_list[i] < 0:
        num_list[i] = -num_list[i]
num_list.sort()
print(num_list)