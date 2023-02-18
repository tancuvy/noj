import pandas as pd

num1 = int(input())
List1 = []
name1 = []
headers = [k for k in input().split()]
for i in range (num1):
    temp = [j for j in input().split()]
    name1.append(temp[0])
    temp.pop(0)
    List1.append(temp)
df1 = pd.DataFrame(List1,index=name1)
df1.columns =  headers
df1 = df1.apply(pd.to_numeric, errors='coerce')
print(df1)
num2 = int(input())
List2 = []
name2 = []
for k in range (num2):
    temp = [g for g in input().split()]
    name2.append(temp[0])
    temp.pop(0)
    List2.append(temp)
name = name1+name2
List = List1+List2
df2 = pd.DataFrame(List,index=name)
df2.columns =  headers
df2 = df2.apply(pd.to_numeric, errors='coerce')
print(df2)



