# Cleaning up data and'skimming/peeing' at data in Python, step by step

# Step 1 is to load the right libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# step 2 is to load up the actual data into a dataframe we will call 'df'
#here is an example without the path: df = pd.read_csv (r'Path where the CSV file is stored\File name.csv') but now for real:

df = pd.read_csv('C:/Users/makeda/programming/fakepatients.csv')

# the next step, step 3, part one, is to check we loaded by looking at say 20 elements- taking a peek
print (df.head(20))

# and/or peek at the end of the list

print(df.tail(20))

#step 4 is to get details on the whole csv table
print('The column names on the table are:',df.columns)
print("The table has x entries with y data points- x,y here are:", df.shape)
print("Let's see the types of data:", df.dtypes)
print("The whole thing is ",df.info)

# step 5 is to look at where we may be able to clean up the data a bit
# let's look at how many duplicates we have (duplicates here meanthe wholeline is duplicated)

df.duplicated().sum()

#  if the sum is above zero- we have a dupe. we can clean it later, but we may want to examine by hand so
#  let's see if we can find where it is manually
if df.duplicated().any() == True:
    print(df)
    
 # we may want to select all duplicate rows based on one column- example here is Patient name
# note the arg keep can be set to 'first', 'last' or False- 
#           keep denotes the occurrence which should be marked as duplicate
#           False - show me all of them
#            default value is ‘first’.
duplicateRowsDF = df[df.duplicated(['Patient name'], keep = False)]
 
print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')

#lets see how many NaNs (here interchangeable with null ) we have in the table
df.isnull().sum()

#let's assume we can drop the duplicates, and do so
df_nodupe = df.drop_duplicates().reset_index(drop = True)

#check the duplicated in the new df
df_nodupe.duplicated().sum()

#drop from the new df the Nans
df_nodupesornans = df_nodupe.dropna()

#verify it is clean
df_nodupesornans.isna().sum()

#let's change the column_names
df_nodupesornans.set_axis(['patient','age','name','condition','image_type','time'], axis= 'columns', inplace = True)

# actually lets also drop the name column, seems like a good idea
df_nodupesornans.drop(columns= 'name')

#show me unique in a column

df_nodupesornans['patient'].unique()

#let's say we want to change a value here, then check by printing the head
df_cleaned= df_nodupesornans.replace('BF6EA5AF', 'crazy_patient')
df_cleaned.head(10)

#let's say we want to change a value here, then check by printing the head
df_cleaned= df_nodupesornans.replace('BF6EA5AF', 'crazy_patient')
df_cleaned.head(10)

#let's sort by some value we care about 
print(df_cleaned.sort_values(by= 'age'))

#let's look at some of the values, and do some basic math and see what we learn
print(df_cleaned['age'].sum())
print(df_cleaned['age'].mean())
print(df_cleaned['age'].max())
print(df_cleaned['age'].min())

# let's start grouping data
grouped_by_condition = df_cleaned.groupby('condition')

#let's count by groups
grouped_by_condition.count()

# lets sum inside groups
grouped_by_condition.sum()

# lets graph it up
aging = df_cleaned.sort_values(by= 'age')
print(aging)
plt.plot('age','time', 'bo', data = aging )

# we found more bad data so now let's really cleean up + graph:
aging.time = pd.to_numeric(aging.time, errors='coerce')
aging.dropna(subset=('time',), inplace=True)
newdf= aging
print(aging.time)
print(newdf)
plt.plot('age','time', 'bo', data = newdf)

#further cleaning
cap_CT= newdf.replace('ct', 'CT')
cap_XR = cap_CT.replace('xr', 'XR')
cleaner = cap_XR.replace('mri', 'MRI')                       
print(cleaner)

#show parameters of new dataframe cleaner
print(cleaner)
print('The column names on the table are:',cleaner.columns)
print("The table has x entries with y data points- x,y here are:", cleaner.shape)
print("Let's see the types of data:", cleaner.dtypes)
print("The whole thing is ",cleaner.info)

#plot with groupby- images versus instances for unique age- here note the highes number is 7, and how whimsical and absurd
cleaner.groupby('image_type')['age'].nunique().plot(kind='bar')
plt.show()
