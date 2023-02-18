#三角函数
import math #math 库
x = int(input())
y = math.radians(x) #角度转换成弧度的函数
z = math.sin(y) + math.cos(y) - math.tan(y/4) * math.tan(y/4)
print('%.4f'%y) #输出四位小数
print('%.4f'%z)