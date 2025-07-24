# Source: https://pandas.pydata.org/docs/reference/api/pandas.concat.html
import pandas as pd
import numpy as np

# *********** CONCAT *************
#concat - Concatenate pandas objects along a particular axis.
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
#s3 = pd.concat([s1, s2])
#s3 = pd.concat([s1, s2], ignore_index=True)
#s3 = pd.concat([s1, s2], keys=['Key1', 'Key2'])
s3 = pd.concat([s1, s2], keys=['Key1', 'Key2'], names=['Series name', 'Row Id'])
#print(s3)

df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
df3 = pd.concat([df1, df2])

df4 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],columns=['letter', 'number', 'animal'])
#df5 = pd.concat([df1, df4])
df5 = pd.concat([df1, df4], join='inner') #defaul join='outer'

df6 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']], columns=['animal', 'name'])
df7 = pd.concat([df1, df6], axis=1) # Combine DataFrame objects horizontally along the x axis by passing in axis=1.

#Prevent the result from including duplicate index values with the verify_integrity option.
df8 = pd.DataFrame([1], index=['a'])
df9 = pd.DataFrame([2], index=['a'])
#df10 = pd.concat([df8, df9], verify_integrity=True) #throws - ValueError: Indexes have overlapping values: Index(['a'], dtype='object')

#Append a single row to the end of a DataFrame object.
df11 = pd.DataFrame({'a': 1, 'b': 2}, index=[0]) #setting index to 0 explicitly
new_row = pd.Series({'a': 3, 'b': 4})
df12 = pd.concat([df11, new_row.to_frame().T], ignore_index=True) #to_frame() turns the Series into a DataFrame with one column per row and .T transposes it

# *********** UNIQUE *************
# Return unique values based on a hash table.
unq = pd.Series([1, 2, 2, 3, 4,4,5,3]).unique()
#print(unq)
unq1 = pd.Series([pd.Timestamp('20250101', tz='US/Eastern'), pd.Timestamp('20250101', tz='US/Eastern')]).unique()
#print(unq1)

# *********** ISNA *************
# Detect missing values for an array-like object.
array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
isNa = pd.isna(array)
print(isNa)

isNa1 = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None, "2017-07-08"])
print(isNa1)

isNa2 = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
print(isNa2)