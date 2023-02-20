# 合并两个有序数组 ，无序用一下sort就完事
list1 = [int(i) for i in input().split(" ")]
list2 = [int(i) for i in input().split(" ")]
list_new = []
i, j = 0,0
while i <len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        list_new.append(list1[i])
        i+=1
    else:
        list_new.append(list2[j])
        j+=1
if i!= len(list1):
    while i < len(list1):
        list_new.append(list1[i])
        i+=1
if j!= len(list2):
    while j < len(list2):
        list_new.append(list2[j])
        j+=1
for item in list_new:
    print(item,end=" ")