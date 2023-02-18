import pandas as pd
data1 = {'Num1':[1,2,5],
        'Num2': [2,3,9],
        'Op': ['plus','power','minus'],
        }
df1 = pd.DataFrame(data1)
print(df1)

data2 = {'Num1':[1,2,5],
        'Num2': [2,3,9],
        'Op': ['plus','power','minus'],
        'result':[3.0,8.0,-4.0],
        }
df2 = pd.DataFrame(data2)
print(df2)