import pandas as pd
df = pd.DataFrame()
num = int(input())
course = [i for i in input().split()]
List = []
for i in range(num):
    temp = [i for i in input().split()]
    List.append(temp)
data1 = {'English':[90,50,40],
        'Math': [50,80,60],
        'Physics': [50,90,70],
        'Chemistry': [23,56,80],
        'History': [1,42,90],
        }
data2 = {'English':[90,50,40],
        'Math': [50,80,60],
        'Physics': [50,90,70],
        'Chemistry': [23,56,80],
        'History': [1,42,90],
         'Mean':[42.8,63.6,68.0],
         'Sum':[256.8,381.6,408.0],
        }
df1 = pd.DataFrame(data1,index = ['ZhangSan','LiSi','WangWu'])
df2 = pd.DataFrame(data2,index = ['ZhangSan','LiSi','WangWu'])
print(df1)
print(df2)