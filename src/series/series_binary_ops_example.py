from unittest.mock import inplace

import pandas as pd
import numpy as np

sr1 = pd.Series(np.random.randint(0, 100, size=10))
#print(sr1)
# sr2 = pd.Series([[5,6,7,8], [1,2,3,4]])
# sr3 = sr1.add(sr2)
# print(sr3[0][0])

sr2 = pd.Series([8,4,5,3,5,3,7,3,2], index=('a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i'))
sr3 = pd.Series([2,3])

sr4 = pd.Series(np.random.rand(5))
sr5 = sr4.round(2)

sr6 = pd.Series(np.random.randint(1, 10, size=5))
sr7 = pd.Series(np.random.randint(0, 10, size=5))
#print(f'Sr6 :\n{sr6}\n')
#print(f'sr7 :\n{sr7}\n')
#print(sr6.product(axis=0))
#print(f'\nDot operation on sr6 and sr7 :\n{sr6.dot(sr7)}')

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])
df3 = df1.dot(df2)
#print(f'DF3 is :\n{df3}')

dt1 = pd.Series([1,2,3])
dt2 = pd.Series([1,1,5])
#print(dt1.dot(dt2))

#************* APPLY ************
ap1 = pd.Series([20, 21, 12], index=['Ottawa', 'Toronto', 'Calgary'])
ap2 = ap1.apply(lambda x: x**2)
#print(ap2)

def sub_cust_value(x, cust_value):
    return x - cust_value

#print(ap1.apply(sub_cust_value, args=(5,)))

def add_cust_value(x, **kwargs):
    for month in kwargs:
        x += kwargs[month]
    return x

#print(ap1.apply(add_cust_value, june=20, july=25, august=30))

#************* AGG ************
#Aggregate using one or more operations over the specified axis.
ag1 = pd.Series([1, 2, 3, 4])
#print(ag1.agg(['min', 'max', 'sum']))

#************ TRANSFORM ***********
#Call func on self producing a Series with the same axis shape as self.
tr = pd.DataFrame({'A': range(3), 'B': range(1, 4)})
#print(tr)
tr1 = tr.transform(lambda x: x * 2)
#print(tr1)

tr2 = pd.Series(range(4))
tr3 = tr2.transform([np.sqrt, np.exp])
#print(tr3)

tr4 = pd.DataFrame({
    "Date": [
        "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05",
        "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05"],
    "Data": [5, 8, 6, 1, 50, 100, 60, 120],
})
tr5 = tr4.groupby('Date')['Data'].transform('sum')
#print(tr5)

tr6 = pd.DataFrame({
    "c": [1, 1, 1, 2, 2, 2, 2],
    "type": ["m", "n", "o", "m", "m", "n", "n"]
})

tr6['size'] = tr6.groupby('c').transform(len)
#print(tr6)

tr7 = pd.DataFrame({
    "c": [1, 1, 1, 2, 2, 2, 2],
    "type": ["m", "n", "o", "m", "m", "n", "n"]
})

tr8 = pd.DataFrame({
    "c": [1, 1, 1, 2, 2, 2, 2],
    "type": ["m", "n", "o", "m", "m", "n", "n"]
})

tr9 = tr7.merge(tr8)

print(tr9[tr9['type'] == 'm'].count())

grp = tr9.groupby('type').sum()
print(grp)

#Find Exercises here
# guipsamora/pandas_exercises
# rishitc/Pandas‑Mini‑Projects
# vi3k6i5/pandas_basics
# mohammadreza‑mohammadi94/Data‑Analysis‑Projects‑With‑Pandas
# tommyod/awesome‑pandas
# felipesebben/Pandas_learning_path
# pandapower
