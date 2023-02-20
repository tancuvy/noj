# 实现栈 用类
class Stack:
    stack = []
    def pop(self):
        self.stack.pop()
    def push(self,i):
        self.stack.append(i)
s = Stack() #栈对象
while True:
    num = [int(i) for i in input().split()] #指令
    print(num)
    if num[0] == 1: # 1是push
        s.push(num[1]) # 跟着的是push的值
    elif num[0] == 2: # 2是pop
        s.pop()
    else:
        break
for i in s.stack: #遍历栈对象
    print(i,end=" ")