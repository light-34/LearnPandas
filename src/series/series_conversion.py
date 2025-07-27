# https://pandas.pydata.org/docs/reference/series.html
import pandas as pd

sr_one = pd.Series([1,2,3,4,5], index=["A","B","C","D","E"])
#this is deep copy but if you add copy(deep=False) it is shallow
sr_two = sr_one.copy()
sr_two.at['A'] = 99
print(f'First Series : \n{sr_one}')
print(f'Second Series : \n{sr_two}')

lst = [1,2,3,4,5]
lst.append(6)
lst1 = lst.copy()
lst1.pop(0)

print(f'First List : \n{lst}')
print(f'Second List : \n{lst1}')
