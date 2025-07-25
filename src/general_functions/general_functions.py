# Source: https://pandas.pydata.org/docs/reference/api/pandas.concat.html
from datetime import date

import pandas as pd
import numpy as np

# *********** CONCAT *************
#concat - Concatenate pandas objects along a particular axis.
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
#s3 = pd.concat([s1, s2])
#s3 = pd.concat([s1, s2], ignore_index=True)
#s3 = pd.concat([s1, s2], keys=['Key1', 'Key2'])
s3 = pd.concat([s1, s2], keys=['Key1', 'Key2'], names=['Series name', 'Row Id'])
#print(s3)

df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
df3 = pd.concat([df1, df2])

df4 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],columns=['letter', 'number', 'animal'])
#df5 = pd.concat([df1, df4])
df5 = pd.concat([df1, df4], join='inner') #defaul join='outer'

df6 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']], columns=['animal', 'name'])
df7 = pd.concat([df1, df6], axis=1) # Combine DataFrame objects horizontally along the x axis by passing in axis=1.

#Prevent the result from including duplicate index values with the verify_integrity option.
df8 = pd.DataFrame([1], index=['a'])
df9 = pd.DataFrame([2], index=['a'])
#df10 = pd.concat([df8, df9], verify_integrity=True) #throws - ValueError: Indexes have overlapping values: Index(['a'], dtype='object')

#Append a single row to the end of a DataFrame object.
df11 = pd.DataFrame({'a': 1, 'b': 2}, index=[0]) #setting index to 0 explicitly
new_row = pd.Series({'a': 3, 'b': 4})
df12 = pd.concat([df11, new_row.to_frame().T], ignore_index=True) #to_frame() turns the Series into a DataFrame with one column per row and .T transposes it

# *********** UNIQUE *************
# Return unique values based on a hash table.
unq = pd.Series([1, 2, 2, 3, 4,4,5,3]).unique()
#print(unq)
unq1 = pd.Series([pd.Timestamp('20250101', tz='US/Eastern'), pd.Timestamp('20250101', tz='US/Eastern')]).unique()
#print(unq1)

# *********** ISNA *************
# Detect missing values for an array-like object.
array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
isNa = pd.isna(array)
#print(isNa)

isNa1 = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None, "2017-07-08"])
#print(isNa1)

isNa2 = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
#print(isNa2)

# *********** ISNULL *************
#Detect missing values for an array-like object.
pd.isna('dog') # False
pd.isna(pd.NA) # True
pd.isna(np.nan) # True

isNl = np.array([[1, np.nan, 4], [2, 5, np.nan]])
#print(isNl)


# *********** TO_NUMERIC *************
#Convert argument to a numeric type.
toNum = pd.Series(['1.2', '3', -5])
#print(pd.to_numeric(toNum)) # default type is float64

toNum1 = pd.Series([1, 2, 3], dtype="Int64")
#print(pd.to_numeric(toNum1, downcast='integer'))



# *********** TO_DATETIME *************
#Convert argument to datetime.
#The keys can be common abbreviations like [‘year’, ‘month’, ‘day’, ‘minute’, ‘second’, ‘ms’, ‘us’, ‘ns’]) or plurals of the same
toDt = df = pd.DataFrame({'year': [2015, 2016],
                        'month': [2, 3],
                        'day': [4, 5]})
dt_conv = pd.to_datetime(df)
#print(dt_conv)

unix_epoch = pd.to_datetime(1490195805, unit='s') #units -> (D,s,ms,us,ns)
unix_ns = pd.to_datetime(1490195805433502912, unit='ns')
#print(unix_epoch)

non_unix = pd.to_datetime([1, 2, 3], unit='D', origin=pd.Timestamp('1960-01-01'))
#print(non_unix)

#python datetime basics https://docs.python.org/3/library/datetime.html#
today = date.today()
#print(today)

dt_format = pd.to_datetime('2018-10-26 12:00:00.0000000011', format='%Y-%m-%d %H:%M:%S.%f') #"%f" will parse all the way up to nanoseconds.
#print(dt_format)

dt_timezone = pd.to_datetime(['2018-10-26 12:00 -0500', '2018-10-26 13:00 -0500'])
#print(dt_timezone)

dt_utc = pd.to_datetime(['2018-10-26 12:00', '2018-10-26 13:00'], utc=True)
#print(dt_utc)

# *********** DATE_RANGE *************
#Return a fixed frequency DatetimeIndex.
rg = pd.date_range(start='1/1/2018', end='1/08/2018')
#print(rg)

rg1 = pd.date_range(
    start=pd.to_datetime("1/1/2018").tz_localize("Europe/Berlin"),
    end=pd.to_datetime("1/08/2018").tz_localize("Europe/Berlin"),
)
#print(rg1)

rg2 = pd.date_range(start='1/1/2018', periods=8) # Specify start and periods, the number of periods (days).
#print(rg2)

rg3 = pd.date_range(start='2018-04-24', end='2018-04-27', periods=3) #Specify start, end, and periods; the frequency is generated automatically (linearly spaced).
#print(rg3)

rg4 = pd.date_range(start='1/1/2018', periods=5, freq='ME') #Changed the freq (frequency) to 'ME' (month end frequency).
#print(rg4)


# *********** PERIOD_RANGE *************
#Return a fixed frequency PeriodIndex.

pd_rg = pd.period_range(start='2017-01-01', end='2018-01-01', freq='M')
#print(pd_rg)

pd_rg1 = pd.period_range(start=pd.Period('2017Q1', freq='Q'), end=pd.Period('2017Q2', freq='Q'), freq='M')
#print(pd_rg1)


# *********** EVAL *************
#Evaluate a Python expression as a string using various backends.
evl_df = df = pd.DataFrame({"animal": ["dog", "pig"], "age": [10, 20]})
evl = pd.eval('double_age = evl_df.age * 2', target=evl_df)
print(evl)






















