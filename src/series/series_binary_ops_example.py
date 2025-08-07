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


#Find Exercises here
# guipsamora/pandas_exercises
# rishitc/Pandas‑Mini‑Projects
# vi3k6i5/pandas_basics
# mohammadreza‑mohammadi94/Data‑Analysis‑Projects‑With‑Pandas
# tommyod/awesome‑pandas
# felipesebben/Pandas_learning_path
# pandapower
