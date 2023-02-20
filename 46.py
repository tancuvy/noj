#算阶乘
import math
class BigInt:
    def __init__(self): #类似？构造方法
        pass
    def calculate(self):
        self.num = int(input())
        self.res = math.factorial(self.num)  #factorial() 方法返回 x 的阶乘
        print(str(self.res))
b = BigInt()
b.calculate()