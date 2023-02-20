# 由0和1组成的二维矩阵，相邻的1可以认为是一个集群，输出矩阵中的集群数量(hint: dfs)
# 集群数也就是找有几个极大连通子图！
n,m = map(int,input().split()) # map会根据提供的函数对指定序列做映射,把input的字符变成int （n行m列的矩阵）
# map()把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。
List = []
for i in range (n):
    temp = [int(j) for j in input().split()] #
    List.append(temp)
def dfs(i,j): #深度优先遍历
    if i<0 or i>=n or j<0 or j>=m:
        return
    if List[i][j] == 0:
        return
    List[i][j] = 0
    dfs(i-1,j)
    dfs(i+1,j)
    dfs(i,j-1)
    dfs(i,j+1)
res = 0
for i in range(n):
    for j in range(m):
        if List[i][j] == 1:
            dfs(i,j)
            res += 1 #递归结束一次 找到一个极大连通子图= 集群数+1
print(res)