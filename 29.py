# 三个人年龄满足规则
age = input()
arr = [int(i) for i in age.split(" ")]
#arr = [int(i) for i in input.split(" ")]
constraint = input()
constraint_list = [int(i) for i in constraint.split(" ")]
# constraint_list = [int(i) for i in input.split(" ")]
sum = 0
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if abs(arr[i] - arr[j]) <= constraint_list[0] and abs(arr[j] - arr[k]) <= constraint_list[1] and abs(
                    arr[i] - arr[k]) <= constraint_list[2]: #abs函数 求绝对值
                sum += 1
print(sum)

