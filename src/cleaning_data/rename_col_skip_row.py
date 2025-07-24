from heapq import nlargest

import pandas as pd

df = pd.read_csv('olympics.csv', header=1) #header is skipping 0 index row
new_names =  {'Unnamed: 0': 'Country',
              '? Summer': 'Summer Olympics',
              '01 !': 'Gold',
                '02 !': 'Silver',
              '03 !': 'Bronze',
             '? Winter': 'Winter Olympics',
             '01 !.1': 'Gold.1',
              '02 !.1': 'Silver.1',
             '03 !.1': 'Bronze.1',
              '? Games': '# Games',
            '01 !.2': 'Gold.2',
               '02 !.2': 'Silver.2',
               '03 !.2': 'Bronze.2'}

df.rename(columns=new_names, inplace=True) # rename the columns
size = 5
print(f' {size} Gold winners : \n{df[df['Gold'] == size]}')

print(f'Max gold winners : \n{df[df['Gold'] == df['Gold'].max()]}')
print(df['Gold'].max())



df2 = df[:145]
print(df2)
nlargest = df2.nlargest(1, 'Gold')
print(f'nlargest () : {nlargest}')

df3 = df[df['Country'].str.startswith(('T', 't'))]
print(df3)
