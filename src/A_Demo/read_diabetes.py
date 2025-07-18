import pandas as pd


df = pd.read_csv('diabetes.csv')
df2 = df.copy()
df2 = df.rename(columns={'DiabetesPedigreeFunction': 'PDF'}, inplace=True)

def read_file():
    return df.head()
    #return df.tail(n = 100)
    #return df.describe()
    #return df.describe(percentiles=[0.3, 0.5, 0.7])
    #return df.describe(include=[int])
    #return df.describe(exclude=[int])
    #return df.info(show_counts=True, memory_usage=True, verbose=True)
    #return df.shape #gets rows and columns df.shape[0] only rows, df.shape[1] only columns
    #return df.columns # shows column names or list(df.columns)


def isolating_column():
    return df['Glucose']
    #return df.describe()
    #return df[['Pregnancies', 'Outcome']] #isoloating many columns
    #return df[df.index == 1] #isolating one row
    #return df[df.index.isin(range(0, 10))] #isolating many rows

def methods_in_use():
    df.index = range(1, 769)
    #return df.loc[2] #uses a label to point to a row, column or cell
    #return df.iloc[0] #uses the numeric position.
    #return df.loc[1:10]
    #return df.iloc[1:10]
    #return df.loc[[10, 15, 20]]
    #return df.loc[100:110, ['Pregnancies', 'BloodPressure', 'Age']]
    #return df.iloc[100:110, :3]
    #return df.loc[750: , ['Pregnancies', 'BloodPressure', 'Age']]
    return df.iloc[750:, :3]

def conditional_slicing():
    #return df[df.BloodPressure == 122]
    return df[df.Glucose > 145]
    #return df.loc[df['Glucose'] > 122, ['Pregnancies', 'Glucose', 'BloodPressure']]

def cleaning_data():
    df.loc[2:5, 'Pregnancies'] = None
    # return df2.head(7)
    # return df2.isnull().head(7)
    # return df2.isnull().sum()
    return df2.isnull().sum().sum()

def dropping_missing_values():
    #df2 = df2.dropna()
    #df2.dropna(inplace=True, axis=1) # inplace -> skip saving the output of .dropna() into a new DataFrame; axis -> dropping rows or columns default to drow rows with NaNs. axis =1 drops column
    df.dropna(inplace=True, how='all') # drops both rows and columns with missing data
    return df2.head()

def replacing_missing_values():
    df3 = df2.copy()
    #mean_value = round(df3['Glucose'].mean(), 2) # only for a column
    mean_value = df3.mean() # mean for all columns
    df3 = df3.fillna((mean_value))
    return mean_value

def duplicate_data():
    df3 = pd.concat([df2, df2])
    df3 = df3.drop_duplicates()
    return df3.shape

def rename_column():
    df2.rename(columns={'DiabetesPedigreeFunction':'PDF', 'BloodPressure':'BP', 'SkinThickness':'ST'}, inplace=True)
    return df2.head()

def sorting_data():
    df.sort_values(by=['Age', 'Glucose'], ascending=[False,True], inplace=True)
    print(df.head(20))

def filtering_data():
    bmiMean = df[(df['Age'] > 50) & (df['Age'] < 68)]['BMI'].mean()
    print(f'BMI mean of ages between 50 and 68 : {bmiMean}')


if __name__ == '__main__':
    print(f'Total 0s in Glucose column: {(df['Glucose'] == 0).sum()}')
    print(df.dropna().count())
    factors = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    #Vectorized replacement very efficien
    df[factors] = df[factors].replace(0, float('nan'))
    #shows how many NaN values there are
    print(df[factors].isna().sum())
    #sort values
    print(df[["Outcome", "Insulin", "Glucose", "BMI", "Age", "Pregnancies"]].sort_values(by='BMI', ascending=False)[:25])

    #Slicing with Condition
    print('********* SLICING *********')
    print(df[df['BMI'] > 30].head(10))
    print('********* ILOC *********')
    print(df[factors].sort_values(by='BMI', ascending=False).iloc[0:20, 1:7])
    print('********* LOC *********')
    print(df.loc[df['Outcome'] == 1, 'Age'])
    print(df.describe(percentiles=[.3, .5, .7])) #Shows 30, 50 70 percentile
    print(df.describe().T)
    print(f'Blood P == 100\n {df[df.BloodPressure == 100]}')
    print(f'Blood P == 100 and Glucose > 95\n {df[(df.BloodPressure == 100) & (df.Glucose > 95)]}')

    print('********* SORT *********')
    sorting_data()

    print(f'Mean Glucose at age 66 : {df[df['Age'] == 66]['Glucose'].mean()}')

    print('********* FILTERING *********')
    bp = df[df['BloodPressure'] > 100].sort_values(by='Age',ascending=False)
    above50 = bp[bp['Age'] >= 50].count()
    print(f'Bp higher 100 in age above 50 : {above50}')
    filtering_data()

    print('********* ISOLATING *********')
    iso = df[df.index.isin(range(0, 20))].copy()
    iso.rename(columns={'DiabetesPedigreeFunction': 'PDF'}, inplace=True)
    iso.sort_values(by='PDF', ascending=False, inplace=True)
    print(iso)





