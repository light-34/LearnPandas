import pandas as pd
import numpy as np

#************ MERGE ***********
tr7 = pd.DataFrame({
    "idx": [1, 2, 3, 4],
    "make": ["Toyota", "Acura", "VW", "BMW"]
})

tr8 = pd.DataFrame({
    "idx": [5, 6, 3, 4],
    "year": [2014, 2015, 2016, 2017],
    "model": ["Prius", "MDX", "id4", "M3"]
})

tr9 = pd.merge(tr7, tr8, on='idx', how='inner') #how= inner, left or right

#print(f'TR9 :\n {tr9}')

#************ AGG ***********
agg = np.arange(20).reshape(4,5)
aggPd = pd.DataFrame(agg)
# print(aggPd)

# print(aggPd.agg(['sum', 'min', 'max']))


#************ TRANSFORM ***********
tr = pd.DataFrame({"A": range(5), "B": range(10, 15)})

def add_five(x):
    return x + 5

tr1 = tr.transform(lambda x: x ** 2)

tr2 = tr.transform(add_five)

# print(tr2)


#************ GROUPBY ***********
gb = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
gbg = gb.groupby('Animal').mean()
# print(gbg)

gbArr = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
          ['Captive', 'Wild', 'Captive', 'Wild']]
gbIdx = pd.MultiIndex.from_arrays(gbArr, names=('Animal', 'Type'))
gb1 = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]}, index=gbIdx)

gbg1 = gb1.groupby(level=0).mean()
gbg2 = gb1.groupby(level='Type').mean()
# print(gb3)

gb4 = [["a", 12, 12], [None, 12.3, 33.], ["b", 12.3, 123], ["a", 1, 1]]
gb5 = pd.DataFrame(gb4, columns=["a", "b", "c"])
gbg3 = gb5.groupby(by='a').sum()
gbg4 = gb5.groupby(by='a', dropna=False).sum()
print(gbg4)

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

