#计算数列值
n = int(input()) #n=3 计算 1+2+3
# and or 都为数字时,and优先级大于or,有and先计算and
# "and"从右往左解析，0为False，1为True。语句中没有0整个句子就为True，但凡有一个为0，整个都是句子就为0
# "or"从左往右解析，找到0了，看下一个数。不是0的话，整条语句就是不是0的那个值。
# print(1 and 3) #3
# print(0 or 3) #3
def sum(n):
    return (n==1 and 1 or n+sum(n-1))
print(sum(n))