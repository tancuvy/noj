#判断字符串里的成分
s = input()
counta = 0
countA = 0
countnum = 0
for i in s:
    if i.islower(): #小写字母 islower
        counta+=1
    elif i.isupper(): #大写字母 isupper
        countA+=1
    elif i.isdigit(): #数字 isdigit
        countnum+=1
    else:
        continue
print(countA,counta,countnum)