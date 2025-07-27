import pandas as pd

# *********** GET *************
# Get item from object for given key (ex: DataFrame column).
df = pd.DataFrame(
    [
        [24.3, 75.7, "high"],
        [31, 87.8, "high"],
        [22, 71.6, "medium"],
        [35, 95, "medium"],
    ],
    columns=["temp_celsius", "temp_fahrenheit", "wind_speed"],
    index=pd.date_range(start="2014-02-12", end="2014-02-15", freq="D"),
)
#print(df.get(["temp_celsius", "wind_speed"]))
ser = df['wind_speed']
#print(ser.get('2014-02-13'))

cars = pd.DataFrame(
    {
        "model": ["Audi", "BMW", "Ford", "Honda"],
        "mpg": [28, 27, 26, 26],
        "cylinders": [4, 4, 3, 3],
        "year": [1999, 2008, 1994, 2013],
    },
    index=[0, 1, 2, 3],
)
#print(cars.get(["model", "year"]))

# *********** AT *************
# Access a single value for a row/column label pair.
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                index=[4, 5, 6], columns=['A', 'B', 'C'])
#print(df.at[4, 'A'])
#print(df.loc[5].at['B'])

# *********** IAT *************
# Access a single value for a row/column pair by integer position.
#print(df.iat[1, 2]) #show 2nd row and 3rd column
df.iat[0, 2] = 10 #change 1st row and 3rd column
#print(df)

# *********** LOC *************
# Access a group of rows and columns by label(s) or a boolean array.
dfl = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
# print(dfl.loc['cobra'])
# print(dfl.loc[['viper', 'sidewinder']]) #[[]] to return a DataFrame
# print(dfl.loc['cobra', 'max_speed']) #index and column returns a single value
# print(dfl.loc['cobra':'viper', 'max_speed'])
# print(dfl.loc[[False, False, True]]) #Boolean list with the same length as the row axis
# print(dfl.loc[dfl['shield'] > 6]) #conditional selection
# print(dfl.loc[(dfl['max_speed'] > 1) & (dfl['shield'] < 8)])
# dfl.loc[['viper', 'sidewinder'], ['shield']] = 50 #assign new values
# print(dfl)
# dfl.loc[:, 'max_speed'] = 30 #assign new values for entire column
# print(dfl)

# *********** ILOC *************
# Purely integer-location based indexing for selection by position.

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
dfil = pd.DataFrame(mydict)
dfil1 = dfil.iloc[0]
print(f'Type of dfil1 : {type(dfil1)}\n {dfil1}')
dfil2 = dfil.iloc[[0,1]]
print(f'Type of dfil2 : {type(dfil2)}\n {dfil2}')
dfil3 = dfil.iloc[:2]
print(f'Type of dfil3 : {type(dfil3)}\n {dfil3}')

# *********** ITEMS *************
# Lazily iterate over (index, value) tuples.
s = pd.Series(['A', 'B', 'C'])
for index, value in s.items():
    print(f'Index : {index} and Value : {value}')

# *********** POP *************
# Return item and drops from series. Raise KeyError if not found.
s = pd.Series([1, 2, 3, 4, 5])
print(s.pop(1))

# *********** XS *************
# Return cross-section from the Series/DataFrame.
# This method takes a key argument to select data at a particular level of a MultiIndex.
d = {'num_legs': [4, 4, 2, 2],
     'num_wings': [0, 0, 2, 2],
     'class': ['mammal', 'mammal', 'mammal', 'bird'],
     'animal': ['cat', 'dog', 'bat', 'penguin'],
     'locomotion': ['walks', 'walks', 'flies', 'walks']}

dfxs = pd.DataFrame(data=d)
dfxs = dfxs.set_index(['class', 'animal', 'locomotion'])
print(dfxs.xs('bird'))

#https://pandas.pydata.org/docs/reference/api/pandas.Series.xs.html
