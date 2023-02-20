# 编辑距离 （插入一个新的 删除一个旧的 把旧的换成新的） 都算一步
# 两个字符分别为A[i],B[j],其中i，j分别表示A,B的第i，j个字符。用d[i][j]表示A字串前i位与B字串前j位的编辑距离
# 当A、B中有一个字串长度为0时，编辑距离d(A,B)等于另一个字符的长度

# 删除操作：相当于d[i-1][j]+1
# 插入操作：相当于d[i][j-1]+1
# 替换操作：
# 当A[i] = B[j]时，相当于d[i-][j-1]+0
# 当A[i]≠B[j]时，相当于d[i-1][j-1]+1
# 即有，d[i][j] = min{d[i-i][j]+1,d[i][j-1]+1,d[i-][j-1]+1} （A[i]≠B[j]）
def EditDist(str1,str2):
    m,n= len(str1)+1,len(str2)+1 #m——>str1 ,n——>str2分别是两个字符串的长度+1
    dp = [[0]*n for i in range (m)] # n列 m维的二维数组 ！表示编辑距离的表格！
    print(dp)
    for i in range (m): #当str2字符为空时，编辑距离为str1的位数
        dp[i][0] = i
    for j in range (n): #当str1字符为空时，编辑距离为str2的位数
        dp[0][j] = j
    dp[0][0] = 0
    for i in range (1,m):
        for j in range (1,n):
            if (str1[i-1] == str2[j-1]):
                dp[i][j] = min(dp[i-1][j-1]+0, dp[i-1][j]+1, dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[m-1][n-1] # 最右下角的dp元素 ，代表二者编辑距离 因为下标从0开始的
s = str(input())
res = EditDist(s,"python")
print(res)



