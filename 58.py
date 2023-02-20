# 请根据每日气温列表，计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用0来代替。
List = [int(i) for i in input().split()]
length = len(List)
res = [0] *(length) #结果列表
for i in range (length):
    for j in range (i+1,length):
        if List[i] < List[j]:
            res[i] = j-i # 间隔多少天
            break
for i in res:
    print(i,end=" ")