import numpy as np

# 读入输入
n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# 计算参数 a 和 b
a, b = np.polyfit(X, Y, 1)

# 输出结果
print(f"{a:.3f} {b:.3f}")