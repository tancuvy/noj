#二进制，八进制和十六进制的转换
a = (int(input(), 2))#输入2进制 转换成10进制比较
b = (int(input(), 8))#输入8进制 转换成10进制比较
c = (int(input()))
d = (int(input(), 16))#输入16进制 转换成10进制比较
max = a
if max<b:
    max = b
if max<c:
    max = c
if max<d:
    max = d
a = bin(max) #10进制转换成2进制
b = oct(max) #10进制转换成8进制
c = max
d = hex(max) #10进制转换成16进制
print("{},{},{},{}".format(a,b,c,d))