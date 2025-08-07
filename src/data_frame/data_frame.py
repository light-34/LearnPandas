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

print(f'TR9 :\n {tr9}')