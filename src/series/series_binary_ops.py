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