count = int(input())
result = ''
while(count >0):
    luoma = input()
    Template = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res = Template[luoma[0]]
    for i in range (1,len(luoma)):
        p = luoma[i-1]
        q = luoma[i]
        if Template[p] <Template[q]:
            res += Template[q] - 2*Template[p]
        else:
            res += Template[q]
    count = count-1
    if(count == 0):
        result = result+str(res)
    else:
        result = result+str(res)+','
print(result)