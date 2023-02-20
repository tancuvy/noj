# 判断从字符串中删掉最多给定整数个字符后能否形成回文字符串
# 本题可转化为求解两个字符串的最长公共子序列（不要求连续） (原字符串和逆置字符串 两个)
# 例 原：abcdeca 与 逆置：acedcba 的最长公共子序列为 5（acdca或aceca），即减掉2个就是回文
# 如果字符串长度都不为0，如果xi=yj，那么最长公共子序列长度为两个字符比较之前的公共子序列的长度+1；
# 如果xi≠yj，那么最长公共子序列的长度为前面字符比较得到的公共子序列的较大值。

def getlcs(str1):
    str1 = list(str1)
    str2 = str1[::-1] #字符串逆置
    length = len(str1)
    dp = [[0 for i in range (length+1)] for j in range (length+1)] #len+1行 len+1列
    for i in range (1,length+1): #0-7 共 8 行
        for j in range (1,length+1) : #0-7 共8列
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else :
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[length][length] # 返回最大公共子序列的长度 len+1*len+1 的表最右下角元素 方法类似编辑距离
s = input()
num = int(input())
res = getlcs(s)
if len(s) - res <= num: #若 len-最大公共子序列长度<= 制定步数
    print("True")
else:
    print("False")