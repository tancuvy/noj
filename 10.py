#罗马数字
count = int(input())
result = ''
while(count >0):
    luoma = input()
    Template = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} #字典类型，有key 和value
    res = Template[luoma[0]] #从罗马字符串第一个开始找对应的数字大小
    for i in range (1,len(luoma)): #目的是加上第二个数字，但是要看第一个和第二个是不是特殊规则的数字
        p = luoma[i-1]
        q = luoma[i]
        if Template[p] <Template[q]:
            res += Template[q] - 2*Template[p] #减去多加的第一次 CM 先加100 再加1000-800 最后=900
        else:
            res += Template[q]
    count = count-1
    if(count == 0):
        result = result+str(res)
    else:
        result = result+str(res)+','
print(result)