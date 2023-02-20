#数组中有两个数字只出现了一次，其他数字都出现了两次，找出来只出现一次的数字（(hint:考虑分组位运算)
List = [int(i) for i in input().split()]
List.sort()
res = []
i = 0
length = len(List)
while i < length:
    count = List.count(List[i])
    if count == 1:
        res.append(List[i])
        i+=1
    else:
        i+=2
print(res)