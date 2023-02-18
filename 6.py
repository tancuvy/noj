#一种简单的加密算法，余数只能是一位
a = int(input())
b = int(input())
c = int(input())
result = (a+b) % c #因为余数只能是一位
print(result*1000)
