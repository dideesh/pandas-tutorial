import numpy as np
import pandas as pd
my_data = [10,20,30]
label = ['a', 'b', 'c']
arr= np.array(my_data)
d={'a':10, 'b': 20, 'c':30}

print(pd.Series(my_data))
print(pd.Series(my_data,label))
print(pd.Series(arr))
print(pd.Series(d))
ser1=pd.Series(d)
print(ser1['c'])

# Let us say we add the states in india by decreasing order of polpulation in millions in 1991 and 2001

State1991=pd.Series([1,2, 3, 4, 5], ['Uttar Pradesh', 'Maharashtra', 'West Bengal', 'Andhra Pradesh', 'Bihar'])
State2001=pd.Series([1, 2, 3, 4, 5], ['Uttar Pradesh', 'Bihar', 'Maharashtra', 'Rajasthan','West Bengal'])

print("State in 1991: ")
print(State1991)
print("State in 2001:")
print(State2001)

print(State1991+State2001)