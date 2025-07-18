import pandas as pd
import numpy as np

#Cleaning data using pandas 
#https://www.datacamp.com/tutorial/pandas

df = pd.read_csv('BL-Flickr-Images-Book.csv') # df = pd.read_csv('BL-Flickr-Images-Book.csv',usecols=) specify columns that you want to use
df.rename(columns={'Edition Statement': 'Ed St', 'Place of Publication': 'PlOf Pub', 'Date of Publication':'DateOf Pub', 'Corporate Contributors':'Corp Cont'}, inplace=True)
# print(list(df.columns))
# print(df.shape)
# print(df.describe())
# print(df.info(show_counts=True, memory_usage=True, verbose=True))
# print(f'Sum of null values in df {df.isnull().sum()}')

#Drop unnecessary columns
to_drop = ['Ed St',
           'Corporate Author',
           'Corp Cont',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']
df.drop(columns=to_drop, inplace=True, axis=1) # axis=1 to drop columns
#print(df.head(10).T)

#Determine a unique column as an index
unique = df['Identifier'].is_unique
#print(unique) #returns True let assign it as index
df.set_index('Identifier', inplace=True)
#print(df.head())

#Get some data
#print(df.loc[206]) # this is name based or df.iloc[0] -> index based

# Tidying up Fields in the Data
#print(df.loc[1905:, 'DateOf Pub'].head(10))

# Remove the extra dates in square brackets, wherever present: 1879 [1878]
# Convert date ranges to their “start date”, wherever present: 1860-63; 1839, 38-54
# Completely remove the dates we are not certain about and replace them with NumPy’s NaN: [1897?]
# Convert the string nan to NumPy’s NaN value
regex = r'^(\d{4})'
extr = df['DateOf Pub'].str.extract(regex, expand=False)
#print(f'Head \n{extr.head()}\n Dtype: \n {extr.dtypes}') #dtype is object we need to convert it to numeric

#assigning numeric verion
df['DateOf Pub'] = pd.to_numeric(extr)
print(df['DateOf Pub'].isnull().sum() / len(df))

#Combining str Methods with NumPy to Clean Columns

# Continue from here https://realpython.com/python-data-cleaning-numpy-pandas/






