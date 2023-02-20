# 判读点是否在圆内 与圆心的距离是否大于半径
class CirCle(object):
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

num = input()
list = [int(i) for i in num.split(" ")]
x1,y1 = list[0],list[1] # 待判断点横纵坐标
x2,y2 = list[2],list[3] # 圆心的横纵坐标
r = list[4] # 半价
c = CirCle(x2,y2,r)
if pow(pow((c.x-x1),2)+pow((c.y-y1),2),0.5) <= c.r: #pow(x,y)方法返回x^y（x 的 y 次方）的值
    print(1) #在圆内
else:
    print(-1)