
# Cleaning up data and'skimming/peeing' at data in Python, step by step
# Step 1 is to load the right libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# step 2 is to load up the actual data into a dataframe we will call 'df'
#here is an example without the path:
#df = pd.read_csv (r'Path where the CSV file is stored\File name.csv') but now for real:

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
