# 实例计数 计算多少个person对象
class Person:
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1
p1 = Person("abc")
p2 = Person("aaa")
p3 = Person("bbb")
p4 = Person("ccc")
p5 = Person("ddd")
print(Person.count)