import pandas as pd
import numpy as np

# Create a sample DataFrame with some outliers
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'age': [25, 32, 28, 45, 22, 38, 95, 31, 29, 41],  # 95 is an outlier
    'salary': [50000, 62000, 55000, 80000, 48000, 71000, 60000, 200000, 59000, 75000], # 200000 is an outlier
    'hours_worked': [40, 42, 38, 45, 39, 41, 37, 40, 2, 43] # 2 is an outlier
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Calculate Q1, Q3, and IQR for each column
#calculates the first quartile (Q1) for the specified columns
Q1 = df[['age', 'salary', 'hours_worked']].quantile(.25)
#calculates the third quartile (Q3)
Q3 = df[['age', 'salary', 'hours_worked']].quantile(.75)
print(Q1)
print(Q3)

#Interquartile Range (IQR) Method
#calculates the Interquartile Range
IQR = Q3 - Q1

# Define the outlier boundaries
lower_bound = Q1 - 1.5 * IQR
print('Lower\n')
print(lower_bound)
upper_bound = Q3 + 1.5 * IQR
print('Upper\n')
print(upper_bound)

#The ~ operator negates the condition, so we are keeping the rows that are not outliers.
# any(axis=1) checks for outliers across any of the selected columns for each row.
df_cleaned = df[~((df[['age', 'salary', 'hours_worked']] < lower_bound) |
                  (df[['age', 'salary', 'hours_worked']] > upper_bound)).any(axis=1)]

print("\nDataFrame after removing outliers:")
print(df_cleaned)