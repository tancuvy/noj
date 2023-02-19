# 闭包：外层函数返回一个内层函数就是闭包
# 计算一个数的立方和平方 用闭包
n = int(input()) #计算n的平方和立方
def outer(n):
    m = [n] #m是个列表 只有一个元素,就是 n. 第一个位置就是 n
    print(m)
    def inner():
        m[0] = m[0]*n #n*n
        return m[0]
    return inner
b = outer(n)
print(b()) #n*n
print(b()) #n*n*n