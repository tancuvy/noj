# 3个元素凑小于目标值的小组 求组数
List = [int(i) for i in input().split()]
target = int(input())
res = 0
length = len(List)
for i in range (length):
    for j in range (i+1,length):
        for k in range (j+1,length):
            if List[i]+List[j]+List[k] < target:
                res+=1
print(res)