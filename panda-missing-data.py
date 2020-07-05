import numpy as np
import pandas as pd

# creating a database with missing values

d={'A':[1,2,np.nan], 'B':[6,np.nan,np.nan], 'C':[1,2,3]}
df=pd.DataFrame(d)
# print(df)

# 'dropna' will drop the colomns with null values and values on rowes can be selected by adding Axis

print(df.dropna())

# Thresold can be added with thresh
print(df.dropna(thresh=2))
# Also values can be filled with the value using 'fillna'
print(df.fillna(value=0))

print(df['A'].fillna(value=df['A'].mean()))

# print(df)