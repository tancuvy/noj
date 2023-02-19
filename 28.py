#逆时针原地旋转一个矩阵（图像）
n = int(input())
martix = []
for i in range (n):
    a = input()
    list = [int(i) for i in a.split(" ")]
    martix.append(list) #生成一个矩阵 （输入） 其实是种2维列表 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#矩阵转置
for i in range (len(martix[0])):#列数 列表第一个成员的元素个数
    for j in range (i,len(martix)):#行数 列表成员数
        martix[i][j],martix[j][i] = martix[j][i],martix[i][j]

martix = martix[::-1] #整个逆置

for i in range(n):
    for j in range(n):
        print(martix[i][j],end=' ')
    print(" ")