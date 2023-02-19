#解方程 x^2 = N

import math
n = int(input())
m = math.sqrt(n) #sqrt函数 开方
m = m * 10000
m = math.floor(m) #floor 函数向下取整
m = m / 10000
print(m)
# round(a,2) 内置函数 保留指定小数位 对a保留两位小数 按四舍五入规则