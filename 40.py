n = int(input())
a = input()
a_list = [int(i) for i in a.split(' ')]
b_list = []
i = 0
while i < len(a_list):
    c_list = []
    c_list.append(a_list[i])
    c_list.append(a_list[i + 1])
    i = i + 2
    b_list.append(c_list)
print(b_list)
b_list.sort()
print(b_list)
i = 0
while i < len(b_list) - 1:
    m = b_list[i]
    n = b_list[i + 1]
    if m[1] < n[0] :
        i = i + 1
    else:
        b_list[i][1] = max(n[1],m[1])
        del b_list[i + 1]
        continue
for i in b_list:
    print(i[0],i[1],end=' ')