# https://pandas.pydata.org/docs/reference/series.html
import pandas as pd

# Attributes
sr_one = pd.Series([[1,2,3,4,5], [6,7,8,9,0]])
print(f'Index : {sr_one.index}')
print(f'Array : {sr_one.array}')
print(f'Values : {sr_one.values}')
print(f'Dtypes : {sr_one.dtype}')
print(f'Shape: {sr_one.shape}')
print(f'Nbytes : {sr_one.nbytes}')
print(f'Ndim : {sr_one.ndim}')