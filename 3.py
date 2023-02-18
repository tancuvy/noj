# n位长的m的二进制数
m=int(input()) #m的二进制
n=int(input()) #n位的长度
res = ''
while m > 0:
    res += str(m%2)
    m = m//2
while len(res)<n:
    res+=str(0)
print(res[::-1])