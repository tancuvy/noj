#给定有序数组 找目标
num = input()
nums = [int(i) for i in num.split(" ")]
target = int(input())
def findindex(a,b):
    for i in range(0,len(b)):
        if b[i] == a:
            return i
        else:
            continue
    return -1
res = findindex(target,nums)
print(res)