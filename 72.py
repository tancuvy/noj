import pandas as pd

df = pd.DataFrame()
data = {'A':[0,4,6,7,8],
        'B': [9,8,3,5,5],
        }

df = pd.DataFrame(data,index=[1,2,1,0,0])
print(df)