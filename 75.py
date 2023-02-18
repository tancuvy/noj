import pandas as pd

df = pd.DataFrame()
List = []
headers = ['Mon','Group','Sales']
for i in range (9):
    temp = [j for j in input().split()]
    List.append(temp)
df = pd.DataFrame(List)
df.columns =  headers
df['Mon'] = df['Mon'].apply(pd.to_numeric, errors='coerce')
df['Sales'] = df['Sales'].apply(pd.to_numeric, errors='coerce')
print(df.groupby('Group')['Sales'].sum())
print(df.groupby('Mon')['Sales'].sum())
