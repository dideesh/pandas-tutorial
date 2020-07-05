import numpy as np
import pandas as pd
from numpy.random import randn
# Indexs=x levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside= [1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)

#diplay
print(outside)
print(inside)
print(hier_index)

# let us create a database with index (5,2)
df1=pd.DataFrame(randn(6,2),hier_index)
print(df1)
df=pd.DataFrame(randn(6,2), hier_index, ['A', 'B'])
print(df)

# Calling data from multilevel index

print(df.loc['G2'].loc[3]['B'])

# Crosssection
print(df.xs(1,level=1))
