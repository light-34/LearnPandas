import pandas as pd
import numpy as np

# Sample raw data
data = {
    'employee_id': ['101', '102', '103', '104', '105', '102'],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Bob'],
    'department': ['HR', 'Engineering', 'Sales', 'Engineering', np.nan, 'Engineering'],
    'salary': ['$60000', '85000', '72000', '90000', '65000', '85000'],
    'start_date': ['2022-01-15', '2021-07-20', '2023-03-10', '2020-11-05', '2022-09-01', '2021-07-20']
}

df = pd.DataFrame(data)
print("Original Raw Data:")
print(df)

# Assess the data
print("Data Info:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")
is_duplicate = df.duplicated()
print(f'Is duplicated : \n {is_duplicate}')
print(f'Duplicated Rows: \n{df[df.duplicated()]}')
