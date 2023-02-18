import pandas as pd

df = pd.DataFrame()
num = int(input())
List = []
name = []
headers = [k for k in input().split()]
for i in range (num):
    temp = [j for j in input().split()]
    name.append(temp[0])
    temp.pop(0)
    List.append(temp)
df = pd.DataFrame(List,index=name)
df.columns =  headers

df = df.apply(pd.to_numeric, errors='coerce')
print(df.info())
print(df.describe())


