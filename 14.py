#递增数组 找目标
num = input()
num_list = [int(i) for i in num.split(",")]
target = int(input())
for i in range (len(num_list)):
    temp = num_list[i]
    if temp < target:
        continue
    else :
        print(i)
        break