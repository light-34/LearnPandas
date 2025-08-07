import pandas as pd
import numpy as np

#************ ADD *************
# Add two Series objects element-wise.
ad = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
ad2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
ad3 = ad.add(ad2, fill_value=0) # null values are filled with 0
#print(ad3)

#************ SUBTRACT *************
#Subtract two Series objects element-wise.
su = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
su2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
su3 = su.sub(su2, fill_value=0) # null values are filled with 0
#print(su3)

#************ MULTIPLY *************
#Multiply two Series objects element-wise.
mu = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
mu2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
mu3 = mu.mul(mu2, fill_value=1) # null values are filled with 1
#print(mu3)

#************ DIVIDE *************
#Divide two Series objects element-wise.
di = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
di2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
di3 = di.div(di2, fill_value=0) # null values are filled with 0
#print(di3)

#************ TRUEDIV *************
#Divide two Series objects element-wise.
tr = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
tr2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
tr3 = tr.truediv(tr2, fill_value=0) # null values are filled with 0
#print(tr3)

#************ FLOORDIV *************
#Return Integer division of series and other, element-wise (binary operator floordiv).
fl = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
fl2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
fl3 = fl.floordiv(fl2, fill_value=0) # null values are filled with 0
print(fl3)

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
