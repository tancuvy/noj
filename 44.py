# 一个类 跟计算器差不多
class Person:
    def __init__(self,name,weight,height,gender):
        self.name = name #右边的是传来的参数  左边的是在类里能用的对象属性
        self.weight = weight
        self.height = height
        self.gender = gender
    def bmi(self):
        if self.gender == 'female':
            return int((self.height - 70)*0.6)
        else:
            return int((self.height - 80)*0.7)
ex_list = [i for i in input().split(" ")]
p = Person(ex_list[0],int(ex_list[1]),int(ex_list[2]),ex_list[3])
print(p.bmi())