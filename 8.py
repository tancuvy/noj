# complex 复数变换
m = complex(input()) #输入的是复数
n = complex(input())
z1 = m + n
print(z1,end = ',')
z2 = m - n
print(z2,end=',')
z3 = m * n
print(z3,end=',')
if(n == 0):
    print("ERROR",end=',')
else:
    z4 = m/n
    print(z4,end=',')
z5 = m.conjugate() #共轭复数
print(z5,end=',')
z6 = abs(m) #模
print(z6)