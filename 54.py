#实现循环队列
n = int(input()) #队列容量
m = int(input()) #操作
a_list = [] #初始队列（带操作）
for i in range(m): #m个操作
    operate = input()
    operate_list = [int(i) for i in operate.split()]
    a_list.append(operate_list)
res_list = []
for c_list in a_list: #遍历a_list的每个元素list
    if c_list[0] == 1:  #push元素
        if len(res_list) < n: #判断还能不能进队列
            res_list.append(c_list[1])
            print('True')
        else:
            print('False')
    else:
        if len(res_list) > 0: # pop元素 #判断还能不能出队列
            element = res_list.pop(0)#pop操作要带出pop的元素是什么
            print(element)
        else:
            print(-1)
print(res_list)