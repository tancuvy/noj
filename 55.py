# 找出数组中和为target的连续子数组
List = [int(i) for i in input().split()]
target = int(input())
count = 0
for i in range (len(List)): #从以第一个元素为开头的子数组
    res = List[i]
    for j in range (i+1,len(List)):
        res += List[j]
        if res == target:
            count += 1
print(count)