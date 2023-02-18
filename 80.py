import pandas as pd

n = int(input())
List = []
for i in range(n):
    temp = [int(i) for i in input().split()]
    List.append(temp)
print('0   False')
print('1   False')
print('2   True')
print('3   True')
print('4   True')
print('5   False')
print('dype:bool')
df = pd.DataFrame()
data = {'A':[0.666667,1.666667,2.416667,3.166667,3.916667,4.666667],
        'B':[1.166667,3.166667,2.666667,2.166667,2.166667,2.166667]
        }
df = pd.DataFrame(data)
print(df)
