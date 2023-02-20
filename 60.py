# 环游世界
# 有n个地点，编号为0到n-1，环游时间从第O天开始，每天都可以环游到一个地点，第0天环游到0号地点，
# 接下来，会有一个环游规则并给一个nextVisit数组。假设某天环游到i号地点，如果算上本次，环游到i号地点的次数为奇数，
# 那么第二天环游到nextVisit[i]指定的地点，0<=next_visit[i]<=i，
# 反之如果是偶数，则访问(i+1)mod n号地点，返回第一次环游完所有地点的时间

next_visit = [int(i) for i in input().split()] #给出nextvisit数组
n = len(next_visit) # n 为数组长度 也就是n个地点数
visited = [0] * n # 存放每个地点的访问次数
i = 0 # 第i = 0天
j = 0 # 第j = 0地点
visited[j] += 1 # 第0天访问第0个地点 此时访问1次 奇数
while True:
    if 0 in visited: # 如果有没被访问过得地点
        if visited[j] % 2 == 1: # 奇数次
            j = next_visit[j] # 奇数次则访问nextvisit数组制定的地方
            i += 1 # 下一天
            visited[j] += 1
        elif visited[j] %2 == 0: #偶数次
            j = (j+1) % n # 偶数次则访问(j+1)modn 号地点
            i += 1 # 下一天
            visited[j] += 1
    else:
        break
print(i) #第一次环游玩所有地方所需的天数