import pandas as pd

df = pd.DataFrame()
data1 = {'Name':['ZhangSan','WangWu','LiSi'],
        'Sex': ['male','female','male'],
        'Age': [15,26,16],
        }
df1 = pd.DataFrame(data1)
print(df1)
data2 = {'Name':['WangWu','ZhangSan'],
        'Weight': [75,150],
        'Height': [150,75],
        }
df2 = pd.DataFrame(data2)
print(df2)
data3 = {'Name':['ZhangSan','WangWu','LiSi'],
        'Sex': ['male','female','male'],
        'Age': [15,26,16],
        'Weight': [150.0,75.0,None],
        'Height': [75.0,150.0,None],
        }
df3 = pd.DataFrame(data3)
print(df3)