# 闭包：外层函数返回一个内层函数 就是闭包
# 闭包是指函数的嵌套，函数内部嵌套一个函数
def outer():
    a = 0
    def inner():
        nonlocal a
        a += 1
        return a
    return inner
b = outer()
for i in range(5):
    print(b())