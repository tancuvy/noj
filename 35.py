def EditDist(str1,str2):
    m,n= len(str1)+1,len(str2)+1
    dp = [[0]*n for i in range (m)]
    for i in range (m): #当str2字符为空时，编辑距离为str1的位数
        dp[i][0] = i
    for j in range (n): #当str1字符为空时，编辑距离为str2的位数
        dp[0][j] = j
    dp[0][0] = 0
    for i in range (1,m):
        for j in range (1,n):
            if ( str1[i-1] == str2[j-1]):
                temp = 0
            else:
                temp = 1
            dp[i][j] = min(dp[i-1][j-1]+temp, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[m-1][n-1]
s = str(input())
res = EditDist(s,"python")
print(res)

