import numpy as np
import pandas as pd
# created a dict for some company, name and revenue
data = {'company':['Google', 'Google', 'Microsoft', 'Microsoft', 'Dell', 'Dell'],
        'person': ['Sam', 'Bill', 'John', 'Adam', 'Victor','Joe'],
        'Sales': [200,100,500,46,150,210]}
df=pd.DataFrame(data)
# print(df)

df_groupby=df.groupby('company')
print(df_groupby.sum())
# now to select a perticular row we can use 'LOC'Function
print ("Sales for Dell is")
print(df_groupby.sum().loc['Dell'])
# or in single line

print(df.groupby('company').sum().loc['Microsoft'])