import pandas as pd

#DataFrame include the following methods

data = pd.read_csv('auto-mpg.csv')

def get_info(dt):
    return dt.info()

def get_shape(dt):
    return dt.shape

def get_columns(dt):
    return dt.columns

def get_mean(dt, column):
    if column == 'All' and is_numeric(dt) and is_column_exists(dt, column):
        print(data.mean())
    elif column != 'All' and is_column_exists(dt, column):
        print(data[column].mean())
    else:
        print("Column not exist or All columns are not numeric")

def get_median(dt): # returns median of the columns
    return dt.median()

def get_maximum(dt):
    return dt.max()

def get_minimum(dt):
    return dt.min()

def get_size(dt):
    return dt.size #Number of elements in the array.

def get_shape(dt):
    return dt.shape #Tuple of array dimension (rows, columns)

def get_array_dimension(dt):
    return dt.ndim #Number of array dimensions.
def is_numeric(dt):
    return dt.map(lambda x: pd.api.types.is_numeric_dtype(type(x))).all().all()

def is_column_exists(dt, column):
    return column in dt.columns

if __name__ == "__main__":
    #print(get_info(data))
    #get_mean(data, 'mpg')
    #print(get_median(data))
    #get_info(data)
    #print(get_maximum(data))
    #print(get_minimum(data))
    array = pd.Series({'a':1, 'b':2, 'c':3})
    df = pd.DataFrame({'c':[1, 2, [3,5,6]], 'd': [4, 5, [1,2,3]], 'b':[7,8,[3,4,5]]})
    #print(get_size(data))
    #print(get_shape(df))
    print(get_array_dimension(df))
