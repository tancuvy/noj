# 有序数组去重
# 请你输入一个有序数组，原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用O(1)额外空间的条件下完成。

List = [int(i) for i in input().split()]
i = 0
while i < len(List):
    count = List.count(List[i])
    if count > 1:
        for k in range(0,count-1): #出现几次删除几-1次
            List.pop(i)
    i+=1 # 代表不同值的元素个数 1 1 2 2 2 4 4 5 5 i就为1 2 3 4
print(len(List))
