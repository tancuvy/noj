a = input()
sum = 0
a_list = [i for i in a.split()]
for i in range(len(a_list)):
    if '.' in a_list[i]: #列表中的元素有没有带点的小数
        try:
            a_list[i] = float(a_list[i])
            sum += a_list[i]
        except:
            continue
    elif a_list[i].isdigit(): #判断是不是数字
        a_list[i] = int(a_list[i])
        sum += a_list[i]
    else:
        continue
print(a_list)
print(sum)