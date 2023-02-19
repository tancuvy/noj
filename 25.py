#只能走一步或走两步 到终点的方式有多少种
n = int(input()) #一共要走多少步
def num(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2 # 1+1  2
    else:
        return num(n-1)+num(n-2)
print(num(n))