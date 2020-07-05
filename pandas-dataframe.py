import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df= pd.DataFrame(randn(5,4),['A','B', 'C', 'D', 'E'],['W','X', 'Y', 'Z'])
print(df)

# Selecting a arow
print(df['X'])

# selecting a value by selecting the row and colomn, the same can also be done for a range
print(df.loc['B','X'])
print(df.loc[('B','C','D'), ('X',  'Y', 'Z')])

# select bool result with a specific condition
bool_df = (df  > 0)
print(bool_df)
print(df[bool_df])
# or
print(df[df>0])
print(df['X']>0)
# the order for filter can be further stacked with []]

# for multiple conditions we ned to use '&' symbol not 'and' and '|' for 'or'
new_df=[(df['W']>0) & (df['Y']>0)]
print(" The value of new_df is")
print(new_df)
print(df)

print(df.reset_index())