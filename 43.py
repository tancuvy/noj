#一个计算器类
class calculate:
    def __init__(self,num1,operator,num2): #初始化 都得有 self类似this
        self.num1 = num1
        self.operator = operator
        self.num2 = num2
    def cal(self):
        if self.operator == "+":
            return self.num1 + self.num2
        elif self.operator == "-":
            return self.num1 - self.num2
        elif self.operator == "*":
            return self.num1 * self.num2
        else:
            return self.num1 // self.num2

num_list = [i for i in input().split(" ")]
ca = calculate(int(num_list[0]),num_list[1],int(num_list[2]))  #这个是对象
print(ca.cal())
