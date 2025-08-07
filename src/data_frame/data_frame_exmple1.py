import pandas as pd
import numpy as np

df = pd.read_csv('../A_Demo/diabetes.csv')
print(df.describe())
np_convert = df.to_numpy()
print(np_convert[0])