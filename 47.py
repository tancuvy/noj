# 朋友圈
# 已知有n个人(编号从0开始)和m对好友关系，如果两个人是直接或间接的好友(好友的好友的好友...）)，则认为他们属于同一个朋友圈，
# 求出这n个人里一共有多少个朋友圈（请定义UnionFindSet并查集类完成求解)。
class unionfindset:
    #初始化并查集，全部填充-1，如果并查集扩大，相应的-1要相加
    def __init__(self, n):
        self.uf = [-1] * (n+1)
        self.set_counts = n
    def find(self, p):
        if self.uf[p] < 0:
            return p
        else:
            self.uf[p] = self.find(self.uf[p])
            return self.uf[p]
    def union(self, p, q):
        #建立一个p->q的连接
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        elif self.uf[qroot] > self.uf[proot]:  #值越小说明树越深，这是两个负数在比较
            self.uf[proot] += self.uf[qroot]
            self.uf[qroot] = proot
            self.set_counts -= 1
        else:
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
            self.set_counts -= 1
    def isconnect(self, p, q):
        return self.find(p) == self.find(q)

n = int(input()) #n个人
m = int(input()) #m对好友关系
a_list = []
for i in range(m):
    x = input()
    y = [int(i) for i in x.split(' ')]
    a_list.append(y)
ut = unionfindset(n)
for i in a_list:
    ut.union(i[0], i[1])
print(ut.set_counts)