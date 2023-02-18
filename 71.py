import pandas as pd

df = pd.DataFrame()
num = int(input())
course = [i for i in input().split()]
res = []
for i in range(num):
        temp = [i for i in input().split()]
        res.append(temp)

data = {'name':['lisi', 'wangwu'],
        'English': [50,40],
        'Math': [80,60],
        'Physics': [90,70],
        'Chemistry': [56, 80],
        'History': [42, 90],
        }
df = pd.DataFrame(data)
print(df)

