import pandas as pd

towns = []
#remove unwanted or extra data
with open('university_towns.txt') as file: #download here https://github.com/realpython/python-data-cleaning/blob/master/Datasets/university_towns.txt
    for line in file:
        if '[edit]' in line:
            state = line
        else:
            towns.append((state, line)) #create a list of tuple

# create a data frame from list
df = pd.DataFrame(towns, columns=['State', 'Region'])

# get rid of useless details using this method in pandas map() function
def get_rid_of_extras(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item


df = df.map(get_rid_of_extras)
#group by data with state
group = df.groupby('State').size()
print(group)