n = int(input())
strlist = [input() for i in range (n)]
public = []
min_str= strlist[0]

for index,item in enumerate(strlist): #遍历列表中的元素和索引
    if len(item) < len(min_str):
        min_str = strlist[index] #找到长度最短的字符串
min_len = len(min_str)
temp = True #如果temp不变说明 有相同前缀

for i in range (min_len):
    for index,item in enumerate(strlist):
        if item[i] != min_str[i]: #有字符不相同
            temp = False #只要有一个字符串中的字符不对应 就直接结束
            break
    if temp:
        public.append(min_str[i])
    else:
        break
res = ''.join(public)
if res == '':
    print("None")
else:
    print(res)


