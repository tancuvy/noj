import pandas as pd
n = int(input())
df = pd.DataFrame()
data1 = {'Mon':[1,1,1,1,1,2,2,2,2,2],
        'Part':['A','B','C','D','E','A','B','C','D','E'],
        'Num':[25,78,45,14,96,48,14,17,74,84],
        'Price':[56,58,78,25,36,68,25,86,35,52]
        }
df1 = pd.DataFrame(data1)
print(df1)
